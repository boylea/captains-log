from django.db import models
from django.utils import timezone


class LogItem(models.Model):
    text = models.TextField()
    event_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
