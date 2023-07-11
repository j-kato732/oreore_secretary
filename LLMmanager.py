import json


class LLMmanager(type):
    """
    LLMmanager class

    This class is a metaclass for LLM (Low Level Model) manager.

    This class is used to manage the functions of the LLM.
    """
    functions = []
    callable_functions = {}

    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if callable(value):
                function_info = {"name": key}
                function_doc = json.loads(value.__doc__)
                function_info.update(function_doc)
                cls.functions.append(function_info)

                cls.callable_functions[key] = value
        return super().__new__(cls, name, bases, attrs)
