from django.conf import settings
from django.db import models
from django.utils import timezone

class CompleteableModel(models.Model):
    completeable = True
    completed_at = models.DateTimeField(null=True)
    wont_do = models.DateTimeField(null=True)

    class Meta:
        abstract = True

    def mark_complete(self):
        self.completed_at = timezone.now()
        self.save()

    def mark_wont(self):
        self.wont_do = timezone.now()
        self.save()

    def unmark_complete(self):
        self.completed_at = None
        self.wont_do = None
        self.save()

class Mission(CompleteableModel):
    name = models.CharField(max_length=255)
    notes = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class LogEntry(models.Model):
    text = models.TextField()
    event_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bullshit_name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completeable = False
    mission = models.ForeignKey(Mission, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text

class ToDoEntry(CompleteableModel):
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mission = models.ForeignKey(Mission, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
