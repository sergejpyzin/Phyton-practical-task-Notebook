import Note


def check_length_message(message):
    while len(message) == 0:
        print("Сообщение должно содержать, как минимум, один символ!")
        message = input(" Попробуйте еще раз. ")
    else:
        return message

def create_note():
    title = check_length_message(input("Введите название заметки: "))
    body = check_length_message(input("Введите содержание заметки: "))
    print("-------------------------------------------")
    print(f"Заметка с наименованием {title} создана")
    return Note.Note(title=title, body=body)

def search_by_title(path):
    searching_title = input("Введите название искомой заметки:\n")
    list_note = File_operation.read_file(path)
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
        File_operation.output_element_to_console(list_note[el_index])
    else:
        print(f"Было найдено {count} заметок с названием '{searching_title}'")
        for element in list_note:
            if element["Название заметки"] == searching_title:
                print(element["ID"] + " " + element["Название заметки"])
        search_by_id(path)