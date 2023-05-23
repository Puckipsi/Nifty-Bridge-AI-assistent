import os
import requests
from urllib.parse import urlparse, unquote
from config import config


def save_file_from_url(url, folder_path):
    response = requests.get(url)

    parsed_url = urlparse(url)
    file_name = unquote(os.path.basename(parsed_url.path))

    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "wb") as file:
        file.write(response.content)

    config.set_env_key('TARGET_SOURCE_FILE_PATH', file_path)


