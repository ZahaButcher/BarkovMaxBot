import asyncio
import logging
import re
from dotenv import load_dotenv
import os
import json
from maxapi import Bot, Dispatcher
from maxapi.types import (
    BotStarted,
    Command,
    MessageCreated,
    CallbackButton,
    MessageCallback,
    BotAdded,
    ChatTitleChanged,
    MessageEdited,
    MessageRemoved,
    UserAdded,
    UserRemoved,
    BotStopped,
    DialogCleared,
    DialogMuted,
    DialogUnmuted,
    ChatButton,  # deprecated: 0.9.14
    MessageChatCreated  # deprecated: 0.9.14
)
from maxapi.utils.inline_keyboard import InlineKeyboardBuilder
load_dotenv()
# Токен берется из переменной окружения
TOKEN = os.environ.get("MAX_BOT_TOKEN")
if not TOKEN:
    raise ValueError("MAX_BOT_TOKEN не установлен!")


bot = Bot(token=TOKEN)
# logging.basicConfig(level=logging.INFO)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

dp = Dispatcher()


numbers = ""
with open("numbers.json", "r", encoding="utf-8") as f:
    numbers = json.load(f)


@dp.message_created(Command('start'))
async def hello(event: MessageCreated):
    if event.message.body.text:
        # await event.message.answer(f"Вы написали: {event.message.body.text}")
        await event.message.answer(f"Здравствуйте!\n"
                                   f"Напиши 'наш 603' или 'наш Захар' и я отвечу наш или не наш.\n"
                                   f"/all - все\n"
                                   f"/family - все наши\n"
                                   f"/blacklist - разыскиваемые гонщики")
    # builder = InlineKeyboardBuilder()
    #
    # builder.row(
    #     CallbackButton(
    #         text='Кнопка 1',
    #         payload='btn_1'
    #     ),
    #     CallbackButton(
    #         text='Кнопка 2',
    #         payload='btn_2',
    #     )
    # )
    # builder.add(
    #     ChatButton(  # deprecated: 0.9.14
    #         text='Создать чат',
    #         chat_title='Тест чат'
    #     )
    # )
    #
    # await event.message.answer(
    #     text='Привет!',
    #     attachments=[
    #         builder.as_markup(),
    #     ]
    # )
@dp.message_created(Command('updatedb'))
async def hello(event: MessageCreated):
    if event.message.body.text:
        # await event.message.answer(f"Вы написали: {event.message.body.text}")
        global numbers

        with open("numbers.json", "r", encoding="utf-8") as f:
            numbers = json.load(f)

        await event.message.answer(f"Данные в базе обновлены!")

@dp.message_created(Command('all'))
async def hello(event: MessageCreated):
    if event.message.body.text:
        stroka = f"All: {len(numbers)}\n"
        for i, j in sorted(numbers.items()):
            stroka += f"{i:<9} - {j['name']}\n"
        # await event.message.answer(f"Вы написали: {event.message.body.text}")
        await event.message.answer(f"{stroka}")

@dp.message_created(Command('family'))
async def hello(event: MessageCreated):
    if event.message.body.text:
        allstroka = f"All: "
        stroka = f""
        count = 0
        for i, j in sorted(numbers.items()):
            if j['name'] not in ["Не пойман", "хз"]:
                count += 1
                stroka += f"{i:<{18 - len(i)}} - {j['name']}\n"
        allstroka += f"{count}\n{stroka}"
        # await event.message.answer(f"Вы написали: {event.message.body.text}")
        await event.message.answer(f"{allstroka}")

@dp.message_created(Command('blacklist'))
async def hello(event: MessageCreated):
    if event.message.body.text:
        stroka = "самых разыскиваемых уличных гонщиков:\n\n"
        count = 0
        for i in sorted(numbers):
            if numbers[i]['name'] in ["Не пойман", "хз"]:
                count += 1
                stroka += f"{i:<{18-len(i)}} - {numbers[i]['marks']}\n"
        # await event.message.answer(f"Вы написали: {event.message.body.text}")
        await event.message.answer(f"{count} {stroka}")

@dp.message_created()  # Я создал, i created
async def start_handler(event: MessageCreated):
    text = event.message.body.text
    if not "наш" in text.lower().split():
        return
    res = ''.join(filter(str.isdigit, text))
    if res == "":
        found = False
        res = re.sub(r'[^a-zA-Zа-яА-ЯёЁ\s]', '', text).lower().replace("наш", "").strip()
        stroka = f"{event.from_user.first_name}, возможно это:\n\n"
        for i, j in sorted(numbers.items()):
            # print(j["name"])
            if res in j["name"].lower():
                found = True
                stroka += f"{i:<{18 - len(i)}} - {j['name']}"
                if j.get("desc"):
                    stroka += f" - '{j.get('desc')}'"
                stroka += "\n"
        await event.message.answer(f"{stroka}") if found else await event.message.answer(f"{event.from_user.first_name}, это не наш!")
        return
    if res.isdigit():
        found = False
        stroka = f"{event.from_user.first_name}, возможно это:\n\n"
        for i, j in sorted(numbers.items()):
            # print(j["name"])
            # if res in j["name"].lower():
            if res in i:
                found = True
                stroka += f"{i:<{18 - len(i)}} - {j['name']}"
                if j.get("desc"):
                    stroka += f" - '{j.get('desc')}'"
                stroka += "\n"

        await event.message.answer(f"{stroka}") if found else await event.message.answer(f"{event.from_user.first_name}, это не наш!")
        return
        # old snizy
        # for i in numbers:
        #     if res in i:
        #         await event.message.answer(f"{event.from_user.first_name}, это {numbers[i]['name']}!")
        #         return

    await event.message.answer(f"{event.from_user.first_name}, это не наш!")

    # await event.message.answer(f"{event.from_user.first_name}, вижу твое сообщение:\n{event.message.body.text}")
    # print(event.message.answer, " // ")
    # print(event)


@dp.bot_added()
async def bot_added(event: BotAdded):
    chat = await event.fetch_chat()
    if chat is None:
        logging.info('Не удалось получить chat, возможно отключен auto_requests!')
        return

    await bot.send_message(
        chat_id=event.chat_id,
        text=f'Привет чат {chat.title}!\nОтправь мне /start, чтобы узнать, что я умею'
    )

# # Реакция на удаленные смс
# @dp.message_removed()
# async def message_removed(event: MessageRemoved):
#     await bot.send_message(
#         chat_id=event.chat_id,
#         text='Я всё видел!'
#     )

# Команда при запуске
@dp.bot_started()
async def bot_started(event: BotStarted):
    await bot.send_message(
        chat_id=event.chat_id,
        text='Привет! Отправь мне /start'
    )

#
# @dp.chat_title_changed()
# async def chat_title_changed(event: ChatTitleChanged):
#     await bot.send_message(
#         chat_id=event.chat_id,
#         text=f'Крутое новое название "{event.title}"!'
#     )
#
#
# @dp.message_callback()
# async def message_callback(event: MessageCallback):
#     await event.answer(
#         new_text=f'Вы нажали на кнопку {event.callback.payload}!'
#     )
#

# @dp.message_edited()
# async def message_edited(event: MessageEdited):
#     await event.message.answer(
#         text='Вы отредактировали сообщение!'
#     )


# @dp.user_removed()
# async def user_removed(event: UserRemoved):
#     from_user = await event.fetch_from_user()
#     if from_user is None:
#         return await bot.send_message(
#             chat_id=event.chat_id,
#             text=f'Неизвестный кикнул {event.user.first_name} 😢'
#         )
#
#     await bot.send_message(
#         chat_id=event.chat_id,
#         text=f'{from_user.first_name} кикнул {event.user.first_name} 😢'
#     )


# @dp.user_added()
# async def user_added(event: UserAdded):
#     chat = await event.fetch_chat()
#     if chat is None:
#         return await bot.send_message(
#             chat_id=event.chat_id,
#             text=f'Чат приветствует вас, {event.user.first_name}!'
#         )
#
#     await bot.send_message(
#         chat_id=event.chat_id,
#         text=f'Чат "{chat.title}" приветствует вас, {event.user.first_name}!'
#     )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
