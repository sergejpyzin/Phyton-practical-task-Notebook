import sys

import FileOperation
import NoteOperation


def greeting():
    print("Добро пожаловать!\nНаше приложение может помочь Вам создавать и редактировать заметки.")
    user_answer = input(
        "Вы хотите продолжить?\nВведите 'Да' для продолжения работы\nВведите 'Нет' для выхода из приложения\n").strip(
        " \n\r")
    if user_answer == "Да".casefold():
        menu()
    elif user_answer == "Нет".casefold():
        sys.exit("Спасибо что воспользовались нашим приложением. До свидания!")
    else:
        print("\033[3m\033[31m{}\033[0m".format("Введенный номер пукта меню несуществует! Попробуйте ещё раз."))
        greeting()

def menu():
    if FileOperation.is_accessible("Notebook.json", mode="r"):
        choice_menu()
    else:
        print("\033[3m\033[31m{}\033[0m".format("Файла для сохранения заметок несуществует! Создайте хотя бы одну заметку."))
        NoteOperation.create_note()
        choice_menu()