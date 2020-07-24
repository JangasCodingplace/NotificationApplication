from django.shortcuts import render

from .models import Notification

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'dashboard/notAuth.html')
    notifications = request.user.notifications_assigned_to_user.order_by('-creation_date')
    old_notifications = notifications.filter(is_read=True)
    unreaded_notifications = notifications.filter(is_read=False).order_by('creation_date')

    context = {
        'unreaded_notification_count':unreaded_notifications.count(),
        'unreaded_notifications':unreaded_notifications[:5],
        'old_notifications':old_notifications[:3]
    }

    return render(request, 'dashboard/index.html', context=context)
