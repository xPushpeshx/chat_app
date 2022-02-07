from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        self.grpname=self.scope['url_route']['kwargs']['gpname']
        await self.channel_layer.group_add(self.grpname,self.channel_name)
        await self.send({
            'type':'websocket.accept'
        })

    
    async def websocket_receive(self,event):
        await self.channel_layer.group_send(self.grpname,{
            'type': 'chat.message',
            'message': event['text']
        })
    
    async def chat_message(self,event):
        await self.send({
            'type':'websocket.send',
            'text': event['message']
        })
    async def websocket_disconnect(self,event):
        await self.channel_layer.group_discard(self.grpname,self.channel_name)
        raise StopConsumer()

     
