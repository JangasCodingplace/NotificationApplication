from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path(
        'ajax/mark_notification_as_readed',
        views.mark_notification_as_readed,
        name='AJAXMarkNotificationAsReaded'
    )
]
