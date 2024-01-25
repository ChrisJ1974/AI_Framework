# data_interpreter_module.py
import openai
from config_module import Config

class DataInterpreterModule:
    def __init__(self):
        config = Config()
        self.api_key = config.get_openai_api_key
        openai.api_key = self.api_key

    def interpret_data(self, data):
        # Use OpenAI API to interpret the data
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",  # or "gpt-3.5-turbo", "gpt-4" based on your access
                prompt=f"Interpret the following data: {data}",
                max_tokens=100
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"An error occurred: {str(e)}"

# Example usage
data_interpreter = DataInterpreterModule()
result = data_interpreter.interpret_data("Your data here")
print(result)
