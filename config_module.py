# config_module.py

class Config:
    def __init__(self):
        self.openai_api_key = 'your API_Key here'

    @property
    def get_openai_api_key(self):
        return self.openai_api_key
    
