from django.shortcuts import render

from .models import Notification

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'dashboard/notAuth.html')
    unreaded_notification_count = Notification.objects.filter(assigned_to=request.user, is_read=False).count()

    context = {
        'unreaded_notification_count':unreaded_notification_count
    }

    return render(request, 'dashboard/index.html', context=context)
