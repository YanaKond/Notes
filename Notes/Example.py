import csv
import os
from datetime import datetime

def read_notes():
    if os.path.exists("notes.csv"):
        with open("notes.csv", "r", newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            notes = list(reader)
        return notes
    else:
        return []

def save_notes(notes):
    with open("notes.csv", "w", newline='', encoding='utf-8') as file:
        fieldnames = ["id", "title", "body", "timestamp"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(notes)

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": len(notes) + 1, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def list_notes():
    for note in notes:
        print(f"{note['id']}. {note['title']} - {note['timestamp']}")

def view_note():
    note_id = int(input("Введите ID заметки: "))
    for note in notes:
        if note['id'] == note_id:
            print(f"Заголовок: {note['title']}")
            print(f"Тело: {note['body']}")
            print(f"Дата/время: {note['timestamp']}")
            break
    else:
        print("Заметка с указанным ID не найдена")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новое тело заметки: ")
            note['title'] = new_title
            note['body'] = new_body
            note['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована")
            break
    else:
        print("Заметка с указанным ID не найдена")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            break
    else:
        print("Заметка с указанным ID не найдена")

def main():
    global notes
    notes = read_notes()
    while True:
        command = input("Введите команду (добавить/список/просмотр/редактировать/удалить/выход): ").lower()
        if command == "добавить":
            add_note()
        elif command == "список":
            list_notes()
        elif command == "просмотр":
            view_note()
        elif command == "редактировать":
            edit_note()
        elif command == "удалить":
            delete_note()
        elif command == "выход":
            break
        else:
            print("Неверная команда")

if __name__ == "__main__":
    main()
