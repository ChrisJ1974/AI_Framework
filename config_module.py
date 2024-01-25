# config_module.py

class Config:
    def __init__(self):
        self.openai_api_key = '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'

    @property
    def get_openai_api_key(self):
        return self.openai_api_key
    