from django.db import models
from django.conf import settings

class Task(models.Model):
    # assigned to user
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks_assigned_to_user"
    )
    # created by user
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks_created_by_user"
    )
    # task title
    title = models.CharField(
        max_length=60
    )
    # task discription
    body = models.TextField(
        blank=True
    )
    # done information
    is_done = models.BooleanField(
        default=False
    )
    # creation date
    creation_date = models.DateTimeField(
        auto_now_add=True
    )

    old_instance = models.ForeignKey(
        'Task',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        editable=False
    )

    def save(self, *args, **kwargs):
        if self.pk is not None:
            self.old_instance = Task.objects.get(pk=self.pk)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"For: {self.assigned_to.username} // id: {self.id}"
