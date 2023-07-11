import json

from LLMmanager import LLMmanager


class MyFunctions(metaclass=LLMmanager):
    @staticmethod
    def get_current_weather(location, unit="fahrenheit"):
        '''
        {
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        }
        '''

        weather_info = {
            "location": location,
            "temperature": "72",
            "unit": unit,
            "forecast": ["sunny", "windy"],
        }
        return json.dumps(weather_info)


my_funcs = MyFunctions()
info = my_funcs.get_current_weather("San Francisco, CA")
print(info)

# 関数のメタデータを取得
print(LLMmanager.functions)

get_current_weather = LLMmanager.callable_functions["get_current_weather"]
print(get_current_weather("San Francisco, CA"))

print(LLMmanager.callable_functions)
