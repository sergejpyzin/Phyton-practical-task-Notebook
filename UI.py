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
        print("\033[3m\033[31m{}\033[0m".format(
            "Файла для сохранения заметок несуществует! Создайте хотя бы одну заметку."))
        NoteOperation.create_note()
        choice_menu()


def choice_menu():
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
    FileOperation.write_note_in_file("Notebook.json")
    choice_menu()


def read_note_menu():
    if FileOperation.file_is_empty("Notebook.json"):
        FileOperation.output_list_note_to_console("Notebook.json")
    else:
        print("\033[3m\033[31m{}\033[0m".format("Файл заметок пуст! Создайте хотя бы одну заметку."))
    choice_menu()


def remove_menu():
    if FileOperation.file_is_empty("Notebook.json"):
        NoteOperation.remove_by_title("Notebook.json")
    else:
        print("\033[3m\033[31m{}\033[0m".format("Файл заметок пуст! Создайте хотя бы одну заметку."))
    choice_menu()


def change_note_menu():
    if FileOperation.file_is_empty("Notebook.json"):
        print("Вы вошли в меню операции по изменению заметок")
        NoteOperation.change_note("Notebook.json")
        search_menu()
    else:
        print("\033[3m\033[31m{}\033[0m".format("Файл заметок пуст! Создайте хотя бы одну заметку."))
    choice_menu()


def search_menu():
    print("+++++++++++++++++++++++++++++++++++++++")
    if FileOperation.file_is_empty("Notebook.json"):
        print("Меню выбора операции поиска заметок")
        answer_from_user = input("Введите номер операции(\n1 - поиск по названию записки\n"
                                 "2 - поиск по слову в составе заметки\n3 - поиск по дате создания/изменения):\n")
        if answer_from_user == "1":
            NoteOperation.search_by_title("Notebook.json")
        elif answer_from_user == "2":
            NoteOperation.search_by_occurrence("Notebook.json")
        elif answer_from_user == "3":
            NoteOperation.search_by_date("Notebook.json")
        else:
            print("\033[3m\033[31m{}\033[0m".format("Введенный номер пукта меню несуществует! Попробуйте ещё раз."))
            search_menu()
    else:
        print("\033[3m\033[31m{}\033[0m".format("Файл заметок пуст! Создайте хотя бы одну заметку."))
        create_menu()
