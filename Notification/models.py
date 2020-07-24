from django.db import models
from django.conf import settings

notification_types = [
    ('c','Task creation info'),
    ('d','Task done info'),
    ('s','System info')
]

class Notification(models.Model):
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications_assigned_to_user"
    )
    group = models.CharField(
        max_length=1,
        choices=notification_types,
        default='s'
    )
    creation_date = models.DateTimeField(
        auto_now_add=True
    )
    is_read = models.BooleanField(
        default=False
    )
    body = models.TextField(
        default='No Description'
    )
    pk_relation = models.IntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"For: {self.assigned_to.username} // id: {self.id}"
