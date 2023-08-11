def check_length_message(message):
    while len(message) == 0:
        print("Сообщение должно содержать, как минимум, один символ!")
        message = input(" Попробуйте еще раз. ")
    else:
        return message