import json
from datetime import datetime

import FileOperation
import Note


def check_length_message(message):
    """Метод check_length_message проверяет сообщение что сообщение от пользователя не пустое.
    Принимает на вход сообщение от пользователя"""
    while len(message) == 0:
        print("Сообщение должно содержать, как минимум, один символ!")
        message = input(" Попробуйте еще раз. ")
    else:
        return message


def create_note():
    """Метод create_note создает экземпляр класса Note."""
    title = check_length_message(input("Введите название заметки: "))
    body = check_length_message(input("Введите содержание заметки: "))
    print("-------------------------------------------")
    print(f"Заметка с наименованием {title} создана")
    return Note.Note(title=title, body=body)






