import json


from testBot import numbers

numbers = dict()

with open("numbers.json", "r", encoding="utf-8") as f:
    numbers = json.load(f)

# stroka = f"All: {len(numbers)}\n"
# for i, j in sorted(numbers.items()):
#     stroka += f"{i} {j['name']}\n"
# print(stroka)


stroka = "самых разыскиваемых уличных гонщиков:\n\n"
count = 0
for i in numbers:
    if numbers[i]['name'] == "Не найден":
        count += 1
        stroka += f"{i} - {numbers[i]['marks']}\n"
print(count, stroka)
exit()
stroka = f"A\n"
for i, j in sorted(numbers.items()):
    stroka += f"{i} {j['name']}\n"