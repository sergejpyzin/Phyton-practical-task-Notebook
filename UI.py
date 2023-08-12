import sys

import FileOperation
import NoteOperation


def greeting():
    """Метод greeting приветствует пользователя и предлагает выбор действия."""
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
    """Метод menu проверяет существует ли файл заметок, в случае отсутствия предлагает создать первую заметку."""
    if FileOperation.file_exists("Notebook.json"):
        choice_menu()
    else:
        print("\033[3m\033[31m{}\033[0m".format(
            "Файла для сохранения заметок несуществует! Создайте хотя бы одну заметку."))
        FileOperation.write_note_in_file("Notebook.json")
        choice_menu()


def choice_menu():
    """Метод choice_menu показывает функционал приложения и предлагает выбор взаимодействия."""
    print("========================================================")
    print("Для продолжения выберете пункт меню\n1 - создание заметки\n2 - редактирование заметки\n3 - поиск заметки\n"
          "4 - удаление заметки\n5 - вывести все заметки\n6 - выход в главное меню")
    answer_from_user = input("Введите номер выбранного пункта меню:\n").strip(" \n\r")
    if answer_from_user == "1":
        create_menu()
    elif answer_from_user == "2":
        change_note_menu()
    elif answer_from_user == "3":
        search_menu()
    elif answer_from_user == "4":
        remove_menu()
    elif answer_from_user == "5":
        read_note_menu()
    elif answer_from_user == "6":
        greeting()
    else:
        print("\033[3m\033[31m{}\033[0m".format("Введённый номер пукта меню несуществует! Попробуйте ещё раз."))
        choice_menu()


def create_menu():
    """Метод create_menu запускает функционал создания заметки."""
    FileOperation.write_note_in_file("Notebook.json")
    choice_menu()


def read_note_menu():
    """Метод read_note_menu запускает функционал чтения всех заметок в файле."""
    if FileOperation.file_is_empty("Notebook.json"):
        FileOperation.output_list_note_to_console("Notebook.json")
    else:
        print("\033[3m\033[31m{}\033[0m".format("Файл заметок пуст! Создайте хотя бы одну заметку."))
    choice_menu()


def remove_menu():
    """Метод remove_menu запускает функционал удаления заметок."""
    if FileOperation.file_is_empty("Notebook.json"):
        FileOperation.remove_by_title("Notebook.json")
    else:
        print("\033[3m\033[31m{}\033[0m".format("Файл заметок пуст! Создайте хотя бы одну заметку."))
    choice_menu()


def change_note_menu():
    """Метод change_note_menu запускает функционал изменения заметок."""
    if FileOperation.file_is_empty("Notebook.json"):
        print("Вы вошли в меню операции по изменению заметок")
        FileOperation.change_note("Notebook.json")
    else:
        print("\033[3m\033[31m{}\033[0m".format("Файл заметок пуст! Создайте хотя бы одну заметку."))
    choice_menu()


def search_menu():
    """Метод search_menu показавает функционал поиска заметок и предлагает выбор взаимодействия."""
    print("+++++++++++++++++++++++++++++++++++++++")
    if FileOperation.file_is_empty("Notebook.json"):
        print("Меню выбора операции поиска заметок")
        answer_from_user = input("Введите номер операции(\n1 - поиск по названию записки\n"
                                 "2 - поиск по слову в составе заметки\n3 - поиск по дате создания/изменения):\n")
        if answer_from_user == "1":
            FileOperation.search_by_title("Notebook.json")
        elif answer_from_user == "2":
            FileOperation.search_by_occurrence("Notebook.json")
        elif answer_from_user == "3":
            FileOperation.search_by_date("Notebook.json")
        else:
            print("\033[3m\033[31m{}\033[0m".format("Введенный номер пукта меню несуществует! Попробуйте ещё раз."))
            search_menu()
    else:
        print("\033[3m\033[31m{}\033[0m".format("Файл заметок пуст! Создайте хотя бы одну заметку."))
        create_menu()
