from _datetime import datetime
import uuid


class Note:
    def __init__(self, title="Text", body="Text"):
        self.title = title
        self.id = str(uuid.uuid4())[0:6]
        self.body = body
        self.date = str(datetime.today().strftime("%d.%m.%Y"))
        self.time = str(datetime.now().time().strftime("%H:%M:%S"))

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_id(self):
        return self.id

    def set_title(self, title):
        self.title = title

    def set_body(self, body):
        self.body = body

    def __str__(self):
        return f"Название заметки {self.title}: \n{self.id}, {self.body}, {self.date}, {self.time}\n"

    def to_dict(self):
        dictionari = {"Название заметки": self.title, "ID": self.id, "Содержание заметки": self.body,
                      "Дата создания/изменения": self.date, "Время создания/изменения": self.time}
        return dictionari
