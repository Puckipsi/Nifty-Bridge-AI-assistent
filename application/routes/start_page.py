from application.services.start_page import StartPageService
from application.__init__ import app, api_router


start_page_service = StartPageService()

api_router.add_api_route(path="/", endpoint=start_page_service.show, methods=["GET"])
app.include_router(api_router)