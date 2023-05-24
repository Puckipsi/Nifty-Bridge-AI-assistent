from dotenv import dotenv_values, set_key


env_values = dotenv_values(".env")


class Config:
    def __init__(self):
        self.OPENAI_API_KEY = env_values.get("OPENAI_API_KEY", "")
        self.OPENAI_MODEL = env_values.get("OPENAI_MODEL", "gpt-3.5-turbo")
        self.OPENAI_TEMPERATURE = env_values.get("OPENAI_TEMPERATURE", 0.0)
        self.OPENAI_MAX_TOKENS = env_values.get("OPENAI_MAX_TOKENS", 4096)
        self.SOURCE_DOC_URL = env_values.get("SOURCE_DOC_URL", "")
        self.SOURCE_DOCS_DIR = env_values.get("SOURCE_DOCS_DIR", "docs")
        self.TARGET_SOURCE_FILE_PATH = env_values.get("TARGET_SOURCE_FILE_PATH", "")
        self.API_KEY = env_values.get("API_KEY", "")
    
    def set_env_key(self, env_key: str, env_value: str):
        env_values[env_key] = env_value
        set_key(".env", env_key, env_values[env_key])


config = Config()
