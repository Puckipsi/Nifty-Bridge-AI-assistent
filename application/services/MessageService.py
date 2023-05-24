from application.models.MessageModel import Message
from fastapi.security.api_key import APIKey
from fastapi import Depends
from . import auth


class MessageService:

    def __init__(self, chatbot: object) -> None:
        self.chatbot = chatbot
    
 
    def send_message(self, message: Message, api_key: APIKey = Depends(auth.get_api_key)):
        question = message.text
        chatbot_answer = self.chatbot.interact_with_user(question)
        
        return {"message": chatbot_answer}
    