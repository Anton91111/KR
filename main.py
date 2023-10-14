import os
import json

def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите текст заметки: ")

    note = {
        "title": title,
        "content": content
    }

    with open("notes.json", "a") as file:
        file.write(json.dumps(note) + "\n")

def read_notes() -> object:
    if not os.path.exists("notes.json"):
        print("У вас еще нет заметок.")
        return

    with open("notes.json", "r") as file:
        for line in file:
            note = json.loads(line)
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['content']}\n")

def edit_note():
    title = input("Введите заголовок заметки, которую хотите отредактировать: ")
    updated_content = input("Введите новый текст заметки: ")

    with open("notes.json", "r") as file:
        lines = file.readlines()

    with open("notes.json", "w") as file:
        for line in lines:
            note = json.loads(line)
            if note['title'] == title:
                note['content'] = updated_content
            file.write(json.dumps(note) + "\n")


def delete_note():
    title = input("Введите заголовок заметки, которую хотите удалить: ")

    with open("notes.json", "r") as file:
        lines = file.readlines()

    with open("notes.json", "w") as file:
        for line in lines:
            note = json.loads(line)
            if note['title'] != title:
                file.write(json.dumps(note) + "\n")


while True:
    print("Выберите действие:")
    print("1. Создать заметку")
    print("2. Просмотреть заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choice = input("Введите номер действия: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("Неправильный выбор. Пожалуйста, выберите снова.")