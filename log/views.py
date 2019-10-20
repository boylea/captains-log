import csv
import datetime

from django.shortcuts import render, get_object_or_404
from .models import LogEntry, ToDoEntry
from .forms import LogEntryForm, ToDoForm
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
    if request.user.is_authenticated:
        if request.method == "POST":
            handle_post(request, (year, month, day))

        entries_for_day = LogEntry.objects.filter(event_date__exact=datetime.date(year, month, day), author=request.user)

        existing_forms = [LogEntryForm(instance=li) for li in entries_for_day]
        new_form = LogEntryForm()
        return render(request, 'log/log_list.html', {'new_form': new_form, 'existing_forms': existing_forms, 'date': (year, month, day)})
    else:
        return redirect('home')

def handle_post(request, date=None, klass=LogEntry, formKlass=LogEntryForm):
    print(request.POST)
    if 'delete_entry' in request.POST:
        post = get_object_or_404(klass, pk=request.POST['delete_entry'])
        post.delete()
        return

    if 'update_entry' in request.POST:
        post = get_object_or_404(klass, pk=request.POST['update_entry'])
        form = formKlass(request.POST, instance=post)
    else:
        # create
        form = formKlass(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        if date:
            year, month, day = date
            post.event_date = datetime.date(year, month, day)
        post.save()

def todo_done(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(ToDoEntry, pk=pk)
        post.mark_complete()
        post.save()
        LogEntry.objects.create(author=request.user, text='Completed: ' + post.text)
        return redirect('todo')
    else:
        return redirect('home')

def todo_undone(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(ToDoEntry, pk=pk)
        post.unmark_complete()
        post.save()
        return redirect('done_todos')
    else:
        return redirect('home')


def todo(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            handle_post(request, klass=ToDoEntry, formKlass=ToDoForm)
        unfinished_todos = ToDoEntry.objects.filter(completed_at__isnull=True, author=request.user)
        existing_forms = [ToDoForm(instance=li) for li in unfinished_todos]
        new_form = ToDoForm()
        return render(request, 'log/todo_list.html', {'new_form': new_form, 'existing_forms': existing_forms})
    else:
        return redirect('home')

def done_todos(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            handle_post(request, klass=ToDoEntry, formKlass=ToDoForm)
        finished_todos = ToDoEntry.objects.filter(completed_at__isnull=False, author=request.user)
        existing_forms = [ToDoForm(instance=li) for li in finished_todos]
        return render(request, 'log/todo_list.html', {'existing_forms': existing_forms})
    else:
        return redirect('home')

def csv_export(request):
    all_log_entries = LogEntry.objects.filter(author=request.user)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="captains_log.csv"'

    writer = csv.writer(response)
    columns = [field.name for field in all_log_entries[0]._meta.get_fields()]
    writer.writerow(columns)
    for entry in all_log_entries:
        row = [request.user.username if name=='author' else entry.serializable_value(name) for name in columns]
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
