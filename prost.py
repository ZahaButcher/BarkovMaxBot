import json
import re


numbers = dict()

with open("numbers.json", "r", encoding="utf-8") as f:
    numbers = json.load(f)
# -----------------------------------------------------

#All users
stroka = f"All: {len(numbers)}\n"
for i, j in sorted(numbers.items()):
    stroka += f"{i:<{18 - len(i)}} - {j['name']}\n"
print(stroka)
exit()
# -----------------------------------------------------
# stroka = "самых разыскиваемых уличных гонщиков:\n\n"
# count = 0
# for i in numbers:
#     if numbers[i]['name'] == "Не найден":
#         count += 1
#         stroka += f"{i:<9} - {numbers[i]['marks']}\n"
# print(count, stroka)
# exit()
# stroka = f"A\n"
# for i, j in sorted(numbers.items()):
#     stroka += f"{i} {j['name']}\n"
#
# ------------------------------------------------------



#search user
text = "наш иван"
# if not "наш" in text.lower():
#     # return
#     pass
# res = ''.join(filter(str.isdigit, text))
# if res == "":
#     # return
#     pass
# for i in numbers:
#     if res in i:
#         await event.message.answer(f"{event.from_user.first_name}, это {numbers[i]['name']}!")
#         # return
# await event.message.answer(f"{event.from_user.first_name}, это не наш!")


#поиск по имени
text = input(": ").lower()

res = ''.join(filter(str.isdigit, text))
print(res)
print(type(res))
if res == "":
    res = re.sub(r'[^a-zA-Zа-яА-ЯёЁ\s]', '', text).lower().replace("наш", "").strip()

    for i, j in numbers.items():
        # print(j["name"])
        if res in j["name"].lower():
            print(f"{i:<9} - {j['name']}")
    exit()

if res.isdigit():
    for i in numbers:
        if res in i:
            print(f"Имя, это {numbers[i]['name']}!")
            exit()




















