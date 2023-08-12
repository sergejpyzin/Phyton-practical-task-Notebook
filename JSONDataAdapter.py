import json

from Note import Note


class JSONDataAdapter:

    @staticmethod
    def to_json(obj):
        """Статический метод to_json принимает на вход экземпляр класса и преобразует его в json-строку"""
        if isinstance(obj, Note):
            return json.dumps({
                "Название заметки": obj.title,
                "ID": obj.id,
                "Содержание заметки": obj.body,
                "Дата создания/изменения": obj.date,
                "Время создания/изменения": obj.time
            })

    @staticmethod
    def from_json(obj):
        """Статический метод from_json принимает на вход json-строку и преобразует её в экземпляр класса"""
        obj = json.loads(obj)
        try:
            title = obj["Название заметки"]
            body = obj["Содержание заметки"]
            note = Note(title, body)
            return note

        except AttributeError:
            print("Неверная структура")
