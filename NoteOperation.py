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