import json
import os

import NoteOperation


def file_is_empty(path):
    if file_exists(path):
        return os.stat(path).st_size != 0


def file_exists(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True


def is_accessible(path, mode="r"):
    try:
        file = open(path, mode)
        file.close()
    except FileNotFoundError:
        return False
    return True


def read_file(path):
    if file_exists(path):
        with open(path) as file:
            return json.load(file)


def write_note_in_file(path):
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
    try:
        file = open(path, "w+")
        file.close()
    except FileNotFoundError:
        print("Создать файл не удалось")


def output_list_note_to_console(path):
    list_note = read_file(path)
    for element in list_note:
        output_element_to_console(element)


def output_element_to_console(element):
    print(f'ID {element["ID"]}, Заметка {element["Название заметки"]}\n '
          f'\tТекст заметки: {element["Содержание заметки"]}'
          f'\n\tДата создания/изменения: {element["Дата создания/изменения"]}, '
          f'Время создания/изменения {element["Время создания/изменения"]};')
