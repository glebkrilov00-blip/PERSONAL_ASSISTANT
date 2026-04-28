data = {
    "notes": ["Купить хлеб", "Выучить Git"], 
    "reminders": [
        {"text": "Позвонить маме", "date": "2026-04-27"},
        {"text": "Сдать проект", "date": "2026-04-30"}
    ]
}

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

    if user_choice == "4":
        print()
        print("Текущие напоминания:\n")
        for num, dict in enumerate(data["reminders"], start=1):
            print(f"{num}. {dict["text"]} ({dict["date"]})")

    if user_choice == "5":
        print()
        new_remind = input("Введите новое напоминание: ")
        new_remind_date = input("Введите дату события (YYYY-MM-DD): ")

        new_dict = {"text": [], "date": []}
        data["reminders"].append(new_dict)
        data["reminders"][2]["text"] = new_remind
        data["reminders"][2]["date"] = new_remind_date
        print()
        print("Текущие напоминания:\n")
        for num, dict in enumerate(data["reminders"], start=1):
            print(f"{num}. {dict['text']} ({dict['date']})")

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

    if user_choice == "7":
        print("Вы вышли из программы!")
        break