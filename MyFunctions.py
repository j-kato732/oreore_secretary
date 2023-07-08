import json

from LLMmanager import LLMmanager


class MyFunctions:
    @LLMmanager.register_function(
        description="Get the current weather in a given location",
        parameters={
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        }
    )
    def get_current_weather(self, location, unit="fahrenheit"):
        """Get the current weather in a given location"""
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
