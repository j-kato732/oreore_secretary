class LLMmanager:
    functions = []

    @staticmethod
    def register_function(description, parameters):
        def _register_decolate(func):
            LLMmanager.functions.append({
                "name": func.__name__,
                "description": description,
                "parameters": parameters,
            })
            return func
        return _register_decolate
