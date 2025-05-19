from channels.generic.websocket import WebsocketConsumer
from account.models import User
import json
from .utils import search
from product.models import Product


class SearchConsumer(WebsocketConsumer):
    def connect(self):
        user: User = self.scope["user"]

        if not user.is_authenticated:
            return self.close()
        
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            self.send(json.dumps({
                "error": "Invalid-Content-Type",
                "message": "Binary data is not accepted."
            }))
            return

        if text_data is None:
             self.send(json.dumps({
                "error": "No-Content",
                "message": "Received empty message."
            }))
             return
        
        try:
            json_data = json.loads(text_data)

        except json.JSONDecodeError:
            self.send(json.dumps({
                "error": "Invalid-JSON",
                "message": "Received data is not valid JSON."
            }))
            return
        
        try:
            search_query = json_data["search_query"]

            if not isinstance(search_query, str) or not search_query.strip():
                 self.send(json.dumps({
                    "error": "Invalid-Input",
                    "message": "'search_query' must be a non-empty string."
                 }))
                 return

            results = search(
                query=search_query,
                model=Product,
                field="name"
            )
            serialized_results = []
            for obj in results[:10]:
                 serialized_results.append({
                      "id": obj.id,
                      "name": getattr(obj, "name")
                 })

            self.send(text_data=json.dumps({
                "success": True,
                "data": serialized_results
            }))

        except KeyError:
            self.send(text_data=json.dumps({
                "error": "Missing-Key",
                "message": "'search_query' key is required in the JSON payload."
            }))

        except Exception as e:
            self.send(text_data=json.dumps({
                "error": "Unknown-Error",
                "message": "An unexpected error occurred on the server.",
                "details": str(e) # SECURITY WARNING: Keep it commented on production 
            }))
