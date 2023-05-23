from application.services.MessageService import MessageService
from application.__init__ import app, api_router
from chatbot.chatbot import ChatBot
from chatbot.vectorestore import VectoreStore


vectorestore = VectoreStore(chunk_size=2500, chunk_overlap=100)
chabot = ChatBot(vectorestore.vectors)
message_service = MessageService(chabot)


api_router.add_api_route(path="/message/send", endpoint=message_service.send_message, methods=["POST"])

app.include_router(api_router)