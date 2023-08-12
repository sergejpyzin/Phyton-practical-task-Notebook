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


def search_by_title(path):
    """Метод search_by_title выполняет поиск заметки по её названию. Принимает на вход путь к файлу"""
    searching_title = input("Введите название искомой заметки:\n")
    list_note = FileOperation.read_file(path)
    count = 0
    el_index = 0
    for element in list_note:
        if element["Название заметки"] == searching_title:
            count += 1
            el_index = list_note.index(element)
    if count == 0:
        print("Не найдено заметок с заданным названием")
    elif count == 1:
        print("------------------------------")
        print(f"Было найдена заметка с названием {searching_title}")
        FileOperation.output_element_to_console(list_note[el_index])
    else:
        print(f"Было найдено {count} заметок с названием '{searching_title}'")
        for element in list_note:
            if element["Название заметки"] == searching_title:
                print(element["ID"] + " " + element["Название заметки"])
        search_by_id(path)


def search_by_id(path):
    """Метод search_by_id выполняет поиск заметки по её ID. Принимает на вход путь к файлу"""
    print("-------------------------------")
    searching_id = input("Введите ID искомой заметки:\n")
    list_note = FileOperation.read_file(path)
    count = 0
    el_index = 0
    for element in list_note:
        if element["ID"] == searching_id:
            count += 1
    if count == 0:
        print("Не найдено заметок с заданным ID!")
    elif count == 1:
        print("------------------------------")
        print(f"Было найдена заметка с ID {searching_id}")
        FileOperation.output_element_to_console(list_note[el_index])


def search_by_date(path):
    """Метод search_by_date выполняет поиск заметки по дате создания или изменения. Принимает на вход путь к файлу"""
    searching_date = input("Введите дату создания/изменения искомой заметки в формате dd.mm.yyyy :\n")
    list_note = FileOperation.read_file(path)
    result_list = []
    for element in list_note:
        if element["Дата создания/изменения"] == searching_date:
            result_list.append(element)
    if len(result_list) == 0:
        print("Не найдено заметок с заданной датой!")
    output_list_to_console(result_list)


def search_by_occurrence(path):
    """Метод search_by_occurrence выполняет поиск заметки по любому слову в составе заметки.
     Принимает на вход путь к файлу"""
    answer_from_user = input("Введите слово которое должно содержаться в составе заметки:\n")
    list_note = FileOperation.read_file(path)
    result_list = []
    for element in list_note:
        if answer_from_user in element["Название заметки"]:
            result_list.append(element)
        elif answer_from_user in element["Содержание заметки"]:
            result_list.append(element)
    if len(result_list) == 0:
        print("\033[3m\033[31m{}\033[0m".format("Заметка содержащая данное слово не найдена!"))
    else:
        output_list_to_console(result_list)


def remove_by_title(path):
    """Метод remove_by_title выполняет удаление заметки по её названию. Принимает на вход путь к файлу"""
    title = input("Введите название заметки которую хотите удалить:\n")
    list_note = FileOperation.read_file(path)
    count = 0
    el_index = 0
    for element in list_note:
        if element["Название заметки"] == title.casefold():
            count += 1
            el_index = list_note.index(element)
    if count == 0:
        print("\033[3m\033[31m{}\033[0m".format("Записок для удаления не найдено."))
    elif count == 1:
        list_note.pop(el_index)
        print(f"Заметка '{title}' удалена")
        with open(path, "w") as fr:
            json.dump(list_note, fr, ensure_ascii=False, indent=2)
    else:
        print(f"Было найдено {count} заметок с названием '{title}'")
        for element in list_note:
            if element["Название заметки"] == title.casefold():
                print(element)
        remove_by_id(path)


def remove_by_id(path):
    """Метод remove_by_id выполняет удаление заметки по её ID. Принимает на вход путь к файлу"""
    being_deleted_id = input("Введите ID заметки которую необходимо удалить:\n")
    list_note = FileOperation.read_file(path)
    for element in list_note:
        if element["ID"] == being_deleted_id:
            el_index = list_note.index(element)
            list_note.pop(el_index)
            print(f"Заметка с ID {being_deleted_id} удалена")
    with open(path, "w") as fr:
        json.dump(list_note, fr, ensure_ascii=False, indent=2)


def change_note(path):
    """Метод change_note выполняет изменение содержания заметки по её названию. Принимает на вход путь к файлу"""
    search_by_title(path)
    list_note = FileOperation.read_file(path)
    id_note = input("Введите ID заметки для редактирования:\n")
    for element in list_note:
        if element["ID"] == id_note:
            element["Содержание заметки"] = input("Введите новое содержание заметки:\n")
            element["Дата создания/изменения"] = str(datetime.today().strftime("%d.%m.%Y"))
            element["Время создания/изменения"] = str(datetime.now().time().strftime("%H:%M:%S"))
            FileOperation.output_element_to_console(element)
    with open(path, "w") as fr:
        json.dump(list_note, fr, ensure_ascii=False, indent=2)


def output_list_to_console(some_list):
    """Метод output_list_to_console вывод в консоль списка словарей. Принимает на вход список словарей"""
    for element in some_list:
        FileOperation.output_element_to_console(element)
