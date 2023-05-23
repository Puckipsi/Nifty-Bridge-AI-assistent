from application.services.MessageService import MessageService
from application.__init__ import app, api_router


message_service = MessageService()


api_router.add_api_route(path="/message/send", endpoint=message_service.send_message, methods=["POST"])

app.include_router(api_router)