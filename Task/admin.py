from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('__str__','created_by','is_done','creation_date',)
    list_filter = ('is_done',)
    search_fields = ('created_by__username', 'assigned_to__username',)

admin.site.register(Task, TaskAdmin)
