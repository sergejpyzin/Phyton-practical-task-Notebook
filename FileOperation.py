import json
import os

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


def output_list_note_to_console(path):
    """Метод output_list_note_to_console выводит на косоль список словарей. Принимает на вход путь к файлу."""
    list_note = read_file(path)
    for element in list_note:
        output_element_to_console(element)


def output_element_to_console(element):
    """Метод output_element_to_console выводит словарь на печать в заданном формате.
    Принимает на вход элемент списка словарей"""
    print(f'ID {element["ID"]}, Заметка {element["Название заметки"]}\n '
          f'\tТекст заметки: {element["Содержание заметки"]}'
          f'\n\tДата создания/изменения: {element["Дата создания/изменения"]}, '
          f'Время создания/изменения {element["Время создания/изменения"]};')
