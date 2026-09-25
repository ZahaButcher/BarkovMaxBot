import json
import re
from itertools import count

numbers = dict()

with open("numbers.json", "r", encoding="utf-8") as f:
    numbers = json.load(f)
# -----------------------------------------------------

#All users
# allstroka = f"All: "
# stroka = f""
# count = 0
# for i, j in sorted(numbers.items()):
#     if j['name'] not in  ["Не пойман", "хз"]:
#         count += 1
#         stroka += f"{i:<{18 - len(i)}} - {j['name']}\n"
# allstroka += f"{count}\n{stroka}"
# print(allstroka)
# exit()
# -----------------------------------------------------
# stroka = "самых разыскиваемых уличных гонщиков:\n\n"
# count = 0
# for i in sorted(numbers):
#     if numbers[i]['name'] in ["Не пойман", "хз"]:
#         count += 1
#         stroka += f"{i:<9} - {numbers[i]['marks']}\n"
# print(count, stroka)
# exit()
# stroka = f"A\n"
# for i, j in sorted(numbers.items()):
#     stroka += f"{i} {j['name']}\n"
# exit()

# ------------------------------------------------------

txt = "Наш вит"
if "наш" in txt.lower().split(" "):
    print(True)
else:
    print(False)

# for i, j in sorted(numbers.items()):
#     if j.get("desc"):
#         print(i, j.get("desc"))
#
#
# exit()
# #search user
# text = "наш иван"
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




















