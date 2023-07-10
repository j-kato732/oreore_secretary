import json


class LLMmanager(type):
    functions = []

    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if callable(value):
                function_info = {"name": key}
                function_doc = json.loads(value.__doc__)
                function_info.update(function_doc)
                cls.functions.append(function_info)
        return super().__new__(cls, name, bases, attrs)
