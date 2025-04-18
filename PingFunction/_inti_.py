import azure.functions as func
from app import app  # Import your Flask app
from azure.functions import WsgiMiddleware

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return WsgiMiddleware(app.wsgi_app).handle(req, context)
