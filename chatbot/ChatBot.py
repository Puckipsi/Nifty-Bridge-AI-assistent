from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import HumanMessage
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationalRetrievalChain

from utils.config import config


class ChatBot:


    def __init__(self, vectors: list):
        self.openai_api_key = config.OPENAI_API_KEY
        self.model_name = config.OPENAI_MODEL
        self.temperature = config.OPENAI_TEMPERATURE
        self.vectors = vectors

    template = """
        You are a helpful AI assistant named Nifty Bridge AI assistant. The user gives you a context, and its content is represented by the following pieces of context. I will use this context to answer the question at the end.
        If you don't know the answer, provide answer "I don't know please contact with support by email support@nifty-bridge.com".
        If the question is not related to the context, politely respond that you are tuned to only answer questions that are related to Nifty Bridge.
        context: {context}
        question: {question}
        """

    PROMPT = PromptTemplate(template=template, input_variables=["context", "question"])

    def interact_with_user(self, question: str):
        print(self.openai_api_key, self.model_name, self.temperature)
        llm = ChatOpenAI(openai_api_key=self.openai_api_key, model_name=self.model_name, temperature=self.temperature)

        retriever = self.vectors.as_retriever()

        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            verbose=True,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": self.PROMPT},
        )
        history = []
        chain_input = ({"question": question, "chat_history":history})
        result = chain(chain_input)
        history.append((chain_input, result))
        return result["answer"]
