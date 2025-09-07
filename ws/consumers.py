import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            "message": "Connected to alerts socket",
            "status" : 200 ,
        }))
        self.running = True
        asyncio.create_task(self.send_updates())

    async def send_updates(self):
        counter = 0
        while self.running:
            counter += 1
            await self.send(text_data=json.dumps({"count": counter}))
            await asyncio.sleep(1)

    async def receive(self, text_data):
        print("hello")


    async def disconnect(self, close_code):
        print("WebSocket disconnected")
