import json
import os
from datetime import datetime

import NoteOperation


def file_is_empty(path):
    """Метод file_is_empty проверяет имеется ли в файле информация. Принимает на вход путь к файлу.
    Если длинна файла неравна нулю возвращает True, в протиположном случае возвращает False"""
    if file_exists(path):
        return os.stat(path).st_size != 0


def file_exists(path):
    """Mетод file_exists проверяет существование файла. Принимает на вход путь к файлу.
    Если необходимый файл существует возвращает True, в протиположном случае возвращает False"""
    try:
        os.stat(path)
    except OSError:
        return False
    return True


def read_file(path):
    """Метод read_file считывает информацию из файла. Принимает на вход путь к файлу. Возвращает json-строку."""
    if file_exists(path):
        with open(path) as file:
            return json.load(file)


def write_note_in_file(path):
    """Метод write_file записывает информацию в файл. Принимает на вход путь к файлу."""
    if file_is_empty(path):
        with open(path) as fr:
            list_obj = json.load(fr)
        list_obj.insert(0, NoteOperation.create_note().to_dict())
    else:
        list_obj = []
        list_obj.insert(0, NoteOperation.create_note().to_dict())
    with open(path, "w") as fr:
        json.dump(list_obj, fr, ensure_ascii=False, indent=2)


def create_file(path):
    """Метод create_file создает файл по указанному пути. Принимает на вход путь к файлу.
    Если создание не получилось выдает сообщение."""
    try:
        file = open(path, "w+")
        file.close()
    except FileNotFoundError:
        print("Создать файл не удалось")


def search_by_title(path):
    """Метод search_by_title выполняет поиск заметки по её названию. Принимает на вход путь к файлу"""
    searching_title = input("Введите название искомой заметки:\n")
    list_note = read_file(path)
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
        output_element_to_console(list_note[el_index])
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
    list_note = read_file(path)
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
        output_element_to_console(list_note[el_index])


def search_by_date(path):
    """Метод search_by_date выполняет поиск заметки по дате создания или изменения. Принимает на вход путь к файлу"""
    searching_date = input("Введите дату создания/изменения искомой заметки в формате dd.mm.yyyy :\n")
    list_note = read_file(path)
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
    list_note = read_file(path)
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
    list_note = read_file(path)
    count = 0
    el_index = 0
    for element in list_note:
        if element["Название заметки"] == title:
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
            if element["Название заметки"] == title:
                print(element)
        remove_by_id(path)


def remove_by_id(path):
    """Метод remove_by_id выполняет удаление заметки по её ID. Принимает на вход путь к файлу"""
    being_deleted_id = input("Введите ID заметки которую необходимо удалить:\n")
    list_note = read_file(path)
    for element in list_note:
        if element["ID"] == being_deleted_id:
            el_index = list_note.index(element)
            list_note.pop(el_index)
            print(f"Заметка с ID {being_deleted_id} удалена")
    with open(path, "w") as fr:
        json.dump(list_note, fr, ensure_ascii=False, indent=2)


def change_note(path):
    """Метод change_note выполняет изменение содержания заметки по её названию. Принимает на вход путь к файлу"""
    list_note = read_file(path)
    title_note = input("Введите название заметки для редактирования:\n")
    count, el_index = 0, 0
    some_list = []
    for element in list_note:
        if element["Название заметки"] == title_note:
            el_index = list_note.index(element)
            some_list.append(list_note[el_index])
            count += 1
    if count == 0:
        print("\033[3m\033[31m{}\033[0m".format("Не найдено заметок с заданным названием"))
    elif count == 1:
        some_dict = list_note[el_index]
        some_dict["Содержание заметки"] = input("Введите новое содержание заметки:\n")
        some_dict["Дата создания/изменения"] = str(datetime.today().strftime("%d.%m.%Y"))
        some_dict["Время создания/изменения"] = str(datetime.now().time().strftime("%H:%M:%S"))
        output_element_to_console(some_dict)
    else:
        output_list_to_console(some_list)
        searching_id = input("Введите ID искомой заметки:\n")
        for element in list_note:
            if element["ID"] == searching_id:
                element["Содержание заметки"] = input("Введите новое содержание заметки:\n")
                element["Дата создания/изменения"] = str(datetime.today().strftime("%d.%m.%Y"))
                element["Время создания/изменения"] = str(datetime.now().time().strftime("%H:%M:%S"))
                output_element_to_console(element)
    with open(path, "w") as fr:
        json.dump(list_note, fr, ensure_ascii=False, indent=2)


def output_list_note_to_console(path):
    """Метод output_list_note_to_console выводит на косоль список словарей. Принимает на вход путь к файлу."""
    list_note = read_file(path)
    for element in list_note:
        output_element_to_console(element)


def output_list_to_console(some_list):
    """Метод output_list_to_console вывод в консоль списка словарей. Принимает на вход список словарей"""
    for element in some_list:
        output_element_to_console(element)


def output_element_to_console(element):
    """Метод output_element_to_console выводит словарь на печать в заданном формате.
    Принимает на вход элемент списка словарей"""
    print(f'ID {element["ID"]}, Заметка {element["Название заметки"]}\n '
          f'\tТекст заметки: {element["Содержание заметки"]}'
          f'\n\tДата создания/изменения: {element["Дата создания/изменения"]}, '
          f'Время создания/изменения {element["Время создания/изменения"]};')
