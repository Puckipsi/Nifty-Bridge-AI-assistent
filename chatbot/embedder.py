from abc import ABC, abstractmethod
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


class FileProcessor(ABC):
    @abstractmethod
    def split_into_chunks(self, file_path, chunk_size):
        pass

    @abstractmethod
    def load_file(self, file_path):
        pass

    @abstractmethod
    def embeddings_store(self, document):
        pass


class FileLoader:
    def load_pdf(self, text_splitter: list, file_path: str):
        loader = PyPDFLoader(file_path=file_path)
        document = loader.load_and_split(text_splitter)
        return document


class EmbedderProcessor(FileProcessor):
    def __init__(self, loader):
        self.loader = loader

    def split_into_chunks(self, file_path:str, chunk_size:int, chunk_overlap:int):
        print(
            f"Splitting file: {file_path} into chunks of size: {chunk_size} with chunk overlap: {chunk_overlap}"
        )

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        return text_splitter

    def load_file(self, text_splitter, file_path: str):
        file_extension = file_path.split(".")[-1]
        if file_extension == "pdf":
            document = self.loader.load_pdf(text_splitter, file_path)
        else:
            print(f"Unsupported file extension: {file_extension}")

        return document

    def embeddings_store(self, document: list):
        embeddings = OpenAIEmbeddings()
        vectors = FAISS.from_documents(document, embeddings)
        return vectors
