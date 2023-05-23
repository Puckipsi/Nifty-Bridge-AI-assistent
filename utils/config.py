from dotenv import dotenv_values


env_values = dotenv_values(".env")


class Config:
    def __init__(self):
        self.OPENAI_API_KEY = env_values.get("OPENAI_API_KEY", "")
        self.OPENAI_MODEL = env_values.get("OPENAI_MODEL", "gpt-3.5-turbo")
        self.OPENAI_TEMPERATURE = env_values.get("OPENAI_TEMPERATURE", 0.0)
        self.OPENAI_MAX_TOKENS = env_values.get("OPENAI_MAX_TOKENS", 4096)
        self.SOURCE_DOC_URL = env_values.get("SOURCE_DOC_URL", "")
        self.SOURCE_DOCS_DIR = env_values.get("SOURCE_DOCS_DIR", "docs")


config = Config()
