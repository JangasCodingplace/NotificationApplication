from django.dispatch import receiver
from django.db.models.signals import post_save
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from Task.models import Task
from .models import Notification

@receiver(post_save, sender=Task)
def create_notification(*args, **kwargs):
    task = kwargs['instance']
    if kwargs['created']:
        if task.created_by != task.assigned_to:
            Notification.objects.create(
                assigned_to = task.assigned_to,
                group='c',
                body=f"{task.created_by.username} created a new task for you! ID: {task.id}",
                pk_relation=task.id
            )
    else:
        if task.created_by != task.assigned_to:
            if task.is_done != task.old_instance.is_done:
                Notification.objects.create(
                    assigned_to = task.created_by,
                    group='d',
                    body=f"Yor created task ID: {task.id} changed his status to {task.is_done}",
                    pk_relation=task.id
                )

@receiver(post_save, sender=Notification)
def send_notification_info(*args, **kwargs):
    if kwargs['created']:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'notification_group', {
                'type':'notification_info'
            }
        )
