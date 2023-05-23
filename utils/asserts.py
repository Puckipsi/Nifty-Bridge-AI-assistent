import os
from config import config
from doc_saver import save_file_from_url


class Verifier:
    @staticmethod
    def openai_api_key_exists():
        api_key = config.OPENAI_API_KEY
        assert api_key, "OpenAI API key not found in .env file"

    @staticmethod
    def source_doc_exists():
        folder_path = os.path.join(config.SOURCE_DOCS_DIR)
        file_path = config.TARGET_SOURCE_FILE_PATH

        if not os.path.isdir(folder_path):
            os.makedirs(folder_path, exist_ok=True)

        if not os.path.exists(file_path):
            save_file_from_url(url=config.SOURCE_DOC_URL, folder_path=folder_path)




