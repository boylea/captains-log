from django.conf import settings
from django.db import models
from django.utils import timezone


class LogEntry(models.Model):
    text = models.TextField()
    event_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bullshit_name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class ToDoEntry(models.Model):
    text = models.TextField()
    completed_at = models.DateTimeField(null=True)
    wont_do = models.DateTimeField(null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_complete(self):
        self.completed_at = timezone.now()
        self.save()

    def unmark_complete(self):
        self.completed_at = None
        self.save()

    def __str__(self):
        return self.text
