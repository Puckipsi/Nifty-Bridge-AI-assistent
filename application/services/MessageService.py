from application.models.MessageModel import Message


class MessageService:

    def __init__(self, chatbot: object) -> None:
        self.chatbot = chatbot
    
 
    def send_message(self, message: Message):
        question = message.text
        chatbot_answer = self.chatbot.interact_with_user(question)
        
        return {"message": chatbot_answer}