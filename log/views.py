from django.shortcuts import render
from .models import LogItem

def log_list(request):
    log_items = LogItem.objects.all();
    return render(request, 'log/log_list.html', {'log_items': log_items})