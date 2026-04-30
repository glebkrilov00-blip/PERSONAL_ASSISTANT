import os
import json
from datetime import date, timedelta

data = {
    "notes": ["Купить хлеб", "Выучить Git"], 
    "reminders": [
        {"text": "Подуть на ветер", "date": "2026-04-29"}, 
        {"text": "Позвонить маме", "date": "2026-04-30"},
        {"text": "Сдать проект", "date": "2026-04-28"},
        {"text": "Переплыть реку", "date": "2026-04-29"}
    ]
}

if os.path.exists ("PERSONAL_ASSISTANT.json") and os.path.getsize("PERSONAL_ASSISTANT.json") > 0:
    with open("PERSONAL_ASSISTANT.json", "r", encoding="utf-8") as a:
        data = json.load(a)
    
    
else:
    with open("PERSONAL_ASSISTANT.json", "x", encoding="utf-8") as c:
        json.dump(data, c, ensure_ascii=False, indent=2)

def save_data():
    with open("PERSONAL_ASSISTANT.json", "w", encoding="utf-8") as d:
            json.dump(data, d, ensure_ascii=False, indent=2)

date_now = date.today().strftime("%Y-%m-%d")
found = False
remind_current = []

for item in data["reminders"]:
    if date_now == item["date"]:
        remind_current.append(item["text"])
        found = True

print("Напоминания на сегодня:\n")
for i, item in enumerate(remind_current, start= 1):
    print(f"{i}. {item}")

if not found:
    print("Напоминаний на сегодня нет!")

while True: 

    user_choice = input("\n---МЕНЮ---\n1. Показать заметки\n2. Добавить заметку\n3. Удалить заметку\n4. Показать напоминания\n5. Добавить напоминание\n6. Удалить напоминание\n7. Выйти\n\nВыберите действие: ")

    if user_choice == "1":
        print()
        print("Текущие заметки:\n")
        c = "\n".join(f"{i}. {items}" for i, items in enumerate(data["notes"], start=1))
        print(f"{c}")

    if user_choice == "2":
        print()
        new_note = input("Введите новую заметку: ")
        data["notes"].append(new_note)
        print("Текущие заметки:\n")
        c = "\n".join(f"{i}. {items}" for i, items in enumerate(data["notes"], start=1))
        print(f"{c}")
        save_data()
            
    if user_choice == "3":
        print()
        c = "\n".join(f"{i}. {items}" for i, items in enumerate(data["notes"], start=1))
        print(f"{c}")
        print()
        note_del = int(input("Какую заметку удалить (введите цифру)? ")) - 1
        del data["notes"][note_del]
        print()
        print("Текущие заметки:\n")
        c = "\n".join(f"{i}. {items}" for i, items in enumerate(data["notes"], start=1))
        print(f"{c}")
        save_data()

    if user_choice == "4":
        print()
        print("Текущие напоминания:\n")
        for num, dict in enumerate(data["reminders"], start=1):
            print(f"{num}. {dict["text"]} ({dict["date"]})")

    if user_choice == "5":
        print()
        new_remind = input("Введите новое напоминание: ")
        new_remind_date = input("Введите дату события (YYYY-MM-DD): ")

        new_dict = {"text": new_remind, "date": new_remind_date}
        data["reminders"].append(new_dict)
        print()
        print("Текущие напоминания:\n")
        for num, dict in enumerate(data["reminders"], start=1):
            print(f"{num}. {dict['text']} ({dict['date']})")
        save_data()

    if user_choice == "6":
        print()
        print("Текущие напоминания:\n")
        for num, dict in enumerate(data["reminders"], start=1):
            print(f"{num}. {dict["text"]} ({dict["date"]})")
        print()
        remind_del = int(input("Какое напоминание удалить (введите цифру)?: ")) - 1
        del data["reminders"][remind_del]
        print()
        print("Текущие напоминания:\n")
        for num, dict in enumerate(data["reminders"], start=1):
            print(f"{num}. {dict["text"]} ({dict["date"]})")
        save_data()

    if user_choice == "7": 
        print("Вы вышли из программы!")
        break