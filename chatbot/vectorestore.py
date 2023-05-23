from .embedder import EmbedderProcessor, FileLoader
from utils.config import config


class VectoreStore:
    def __init__(self, chunk_size: int, chunk_overlap: int) -> None:
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.loader = FileLoader()
        self.processor = EmbedderProcessor(self.loader)

    @property
    def vectors(self):
        file_path = config.TARGET_SOURCE_FILE_PATH
        text_splitter = self.processor.split_into_chunks(
            file_path=file_path,
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
        )

        document = self.processor.load_file(text_splitter, file_path)
        vectors = self.processor.embeddings_store(document)

        return vectors
