import csv
import os
import datetime


def create_note():
    note_id = input("Введите идентификатор заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [note_id, title, body, timestamp]


def load_notes():
    notes = []
    if os.path.exists('notes.csv'):
        with open('notes.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                notes.append(row)
    return notes


class NoteApp:
    def __init__(self):
        self.notes = load_notes()

    def save_notes(self):
        with open('notes.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(self.notes)

    def display_notes(self):
        for note in self.notes:
            print(f"Идентификатор: {note[0]}")
            print(f"Заголовок: {note[1]}")
            print(f"Текст: {note[2]}")
            print(f"Дата/время: {note[3]}")
            print("----------------------")

    def edit_note(self):
        note_id = input("Введите идентификатор заметки для редактирования: ")
        for note in self.notes:
            if note[0] == note_id:
                print(f"Текущий текст заметки: {note[2]}")
                new_body = input("Введите новый текст заметки: ")
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                note[2] = new_body
                note[3] = timestamp
                self.save_notes()
                print("Заметка успешно отредактирована.")
                return
        print("Заметка с указанным идентификатором не найдена.")

    def delete_note(self):
        note_id = input("Введите идентификатор заметки для удаления: ")
        for note in self.notes:
            if note[0] == note_id:
                self.notes.remove(note)
                self.save_notes()
                print("Заметка успешно удалена.")
                return
        print("Заметка с указанным идентификатором не найдена.")

    def read_notes_by_date(self):
        sorted_notes = sorted(self.notes, key=lambda x: x[3])
        for note in sorted_notes:
            print(f"Идентификатор: {note[0]}")
            print(f"Заголовок: {note[1]}")
            print(f"Текст: {note[2]}")
            print(f"Дата/время: {note[3]}")
            print("----------------------")

    def display_selected_note(self, note_id):
        for note in self.notes:
            if note[0] == note_id:
                print(f"Идентификатор: {note[0]}")
                print(f"Заголовок: {note[1]}")
                print(f"Текст: {note[2]}")
                print(f"Дата/время: {note[3]}")
                return
        print("Заметка с указанным идентификатором не найдена.")

    def run(self):
        while True:
            print("Выберите действие:")
            print("1. Просмотреть все заметки")
            print("2. Просмотреть выбранную заметку")
            print("3. Создать новую заметку")
            print("4. Редактировать заметку")
            print("5. Удалить заметку")
            print("6. Выход")

            choice = input("Введите номер действия: ")

            if choice == '1':
                self.read_notes_by_date()
            elif choice == '3':
                new_note = create_note()
                self.notes.append(new_note)
                self.save_notes()
                print("Заметка успешно создана!")
            elif choice == '4':
                self.edit_note()
            elif choice == '5':
                self.delete_note()
            elif choice == '2':
                note_id = input("Введите идентификатор заметки для просмотра: ")
                self.display_selected_note(note_id)
            elif choice == '6':
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

        print("Спасибо за использование приложения заметок!")


# Создание экземпляра класса и запуск приложения
note_app = NoteApp()
note_app.run()
