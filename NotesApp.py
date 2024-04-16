import json
import os
from datetime import datetime

from Note import Note


class NotesApp:
    def __init__(self, storage_file='notes.json'):
        self.storage_file = storage_file
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                self.notes = json.load(file)

    def save_notes(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.notes, file, default=lambda x: x.__dict__, indent=4)

    def add_note(self, title, message):
        note_id = len(self.notes) + 1
        self.notes.append(Note(note_id, title, message))
        self.save_notes()

    def edit_note(self, note_id, title, message):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = title
                note.message = message
                note.timestamp = datetime.now().isoformat()
                break
        self.save_notes()

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.save_notes()

    def list_notes(self, filter_date=None):
        if filter_date:
            filtered_notes = [note for note in self.notes if note.timestamp.startswith(filter_date)]
            for note in filtered_notes:
                print(f"ID: {note.note_id}, Title: {note.title}, Timestamp: {note.timestamp}")
        else:
            for note in self.notes:
                print(f"ID: {note.note_id}, Title: {note.title}, Timestamp: {note.timestamp}")


if __name__ == "__main__":
    notes_app = NotesApp()

    while True:
        command = input("Введите команду (add, edit, delete, list, exit): ").strip().lower()

        if command == "add":
            title = input("Введите заголовок заметки: ").strip()
            message = input("Введите текст заметки: ").strip()
            notes_app.add_note(title, message)
            print("Заметка успешно добавлена.")
        elif command == "edit":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ").strip()
            message = input("Введите новый текст заметки: ").strip()
            notes_app.edit_note(note_id, title, message)
            print("Заметка успешно отредактирована.")
        elif command == "delete":
            note_id = int(input("Введите ID заметки для удаления: "))
            notes_app.delete_note(note_id)
            print("Заметка успешно удалена.")
        elif command == "list":
            filter_date = input(
                "Введите дату для фильтрации (YYYY-MM-DD), или нажмите Enter для вывода всех заметок: ").strip()
            notes_app.list_notes(filter_date)
        elif command == "exit":
            break
        else:
            print("Неверная команда. Пожалуйста, попробуйте снова.")
