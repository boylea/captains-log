from django.contrib import admin
from .models import LogEntry, ToDoEntry

admin.site.register(LogEntry)
admin.site.register(ToDoEntry)
