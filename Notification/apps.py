from django.apps import AppConfig


class NotificationConfig(AppConfig):
    name = 'Notification'

    def ready(self):
        import Notification.signals
