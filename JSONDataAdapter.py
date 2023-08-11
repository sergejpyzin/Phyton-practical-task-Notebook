import json

from Note import Note


class JSON_Data_Adapter:

    @staticmethod
    def to_json(obj):
        if isinstance(obj, Note):
            return json.dumps({
                "Название заметки": obj.title,
                "ID": obj.id,
                "Содержание заметки": obj.body,
                "Дата создания/изменения": obj.date,
                "Время создания/изменения": obj.time
            })