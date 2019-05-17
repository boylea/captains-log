import csv
import datetime

from django.shortcuts import render, get_object_or_404
from .models import LogEntry
from .forms import LogEntryForm
from django.shortcuts import redirect
from django.http import HttpResponse

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

def csv_export(request):
    all_log_entries = LogEntry.objects.filter(author=request.user)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="captains_log.csv"'

    writer = csv.writer(response)
    columns = [field.name for field in all_log_entries[0]._meta.get_fields()]
    writer.writerow(columns)
    for entry in all_log_entries:
        row = [entry.serializable_value(name) for name in columns]
        writer.writerow(row)

    return response


def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entries = LogEntry.objects.filter(text__icontains=query_string).order_by('event_date')
        return render(request, 'log/home.html', { 'query_string': query_string, 'entries': entries })
    else:
        return render(request, 'log/home.html')
