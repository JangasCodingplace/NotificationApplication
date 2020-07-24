from django.contrib import admin
from django.urls import path,include

from Notification import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Notification.urls')),
]
