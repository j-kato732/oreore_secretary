import json


class LLMmanager:
    functions = []

    @staticmethod
    def register_function(func):
        def _register_decolate(*args, **kwargs):
            function_name = {"name": func.__name__}
            function_info = json.loads(func.__doc__)
            function_name.update(function_info)
            LLMmanager.functions.append(function_name)

            return func(*args, **kwargs)
        return _register_decolate
