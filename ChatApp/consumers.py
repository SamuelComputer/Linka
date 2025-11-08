import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from ChatApp.models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_data = text_data_json

        # Broadcast message to all clients in the room
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'send_message',
                'message': message_data
            }
        )

    async def send_message(self, event):
        data = event['message']
        msg_obj = await self.create_message(data=data)

        response_data = {
            'sender': data['sender'],
            'message': msg_obj.message,
            'file': None  # 👈 no file uploads
        }

        await self.send(text_data=json.dumps({'message': response_data}))

    @database_sync_to_async
    def create_message(self, data):
        room = Room.objects.get(room_name=data['room_name'])
        message_text = data.get('message', '')
        msg = Message.objects.create(
            room=room,
            sender=data['sender'],
            message=message_text
        )
        return msg
