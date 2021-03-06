# Generated by Django 3.0.8 on 2020-07-24 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('c', 'Task creation info'), ('d', 'Task done info'), ('s', 'System info')], default='s', max_length=1)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('body', models.TextField(default='No Description')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_assigned_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
