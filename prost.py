import json

with open("numbers.json", "r", encoding="utf-8") as f:
    numbers = json.load(f)

stroka = f"All: {len(numbers)}\n"
for i, j in sorted(numbers.items()):
    stroka += f"{i} {j['name']}\n"
print(stroka)