import datetime

from django.shortcuts import render, get_object_or_404
from .models import LogEntry
from .forms import LogEntryForm
from django.shortcuts import redirect

def log_list(request):
    print(request)
    if request.method == "POST":
        handle_post(request)
    log_entries = LogEntry.objects.all();
    existing_forms = [LogEntryForm(instance=li) for li in log_entries]
    new_form = LogEntryForm()
    return render(request, 'log/log_list.html', {'new_form': new_form, 'existing_forms': existing_forms, 'date': []})

def home(request):
    return render(request, 'log/home.html')

def log_day(request, year, month, day):
    print("user:", request.user.pk)
    if request.method == "POST":
        handle_post(request, (year, month, day))

    entries_for_day = LogEntry.objects.filter(event_date__exact=datetime.date(year, month, day), author=request.user)

    existing_forms = [LogEntryForm(instance=li) for li in entries_for_day]
    new_form = LogEntryForm()
    return render(request, 'log/log_list.html', {'new_form': new_form, 'existing_forms': existing_forms, 'date': (year, month, day)})

def handle_post(request, date=None):
    print(request.POST)
    if 'delete_entry' in request.POST:
        post = get_object_or_404(LogEntry, pk=request.POST['delete_entry'])
        post.delete()
        return

    if 'update_entry' in request.POST:
        post = get_object_or_404(LogEntry, pk=request.POST['update_entry'])
        form = LogEntryForm(request.POST, instance=post)
    else :
        form = LogEntryForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        if date:
            year, month, day = date
            post.event_date = datetime.date(year, month, day)
        post.save()