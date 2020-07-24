from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from django.core import serializers

class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self, event):
        print("CONNECTED", event)

        await self.channel_layer.group_add(
            f"notification_group_{self.scope['url_route']['kwargs']['user_id']}",
            self.channel_name
        )

        await self.accept()
        
        context = await self.get_notification_info(self.scope)

        await self.send_json(content=context)

    async def websocket_disconnect(self, event):
        print("DISCONNECTED", event)

    async def websocket_receive(self, event):
        print("RECEIVE", event)
        await self.send(text_data='HELLO')

    async def notification_info(self,event):
        context = await self.get_notification_info(self.scope)

        await self.send_json(content=context)

    @database_sync_to_async
    def get_notification_info(self,scope):
        if not scope['user'].is_authenticated:
            context = {
                'unreaded_notification_count':'',
                'unreaded_notifications':'',
                'old_notifications':''
            }
            return context

        notifications = scope['user'].notifications_assigned_to_user.order_by('-creation_date')
        old_notifications = notifications.filter(is_read=True)
        unreaded_notifications = notifications.filter(is_read=False).order_by('creation_date')

        context = {
            'unreaded_notification_count':unreaded_notifications.count(),
            'unreaded_notifications':serializers.serialize('json',unreaded_notifications),
            'old_notifications':serializers.serialize('json',old_notifications[:3])
        }

        return context