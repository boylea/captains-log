import datetime

from django.shortcuts import render, get_object_or_404
from .models import LogItem
from .forms import LogItemForm
from django.shortcuts import redirect

def log_list(request):
    print(request)
    if request.method == "POST":
        handle_post(request)
    log_items = LogItem.objects.all();
    existing_forms = [LogItemForm(instance=li) for li in log_items]
    new_form = LogItemForm()
    return render(request, 'log/log_list.html', {'new_form': new_form, 'existing_forms': existing_forms, 'date': []})

def log_day(request, year, month, day):
    print(year, month, day)
    if request.method == "POST":
        handle_post(request, (year, month, day))

    items_for_day = LogItem.objects.filter(event_date__exact=datetime.date(year, month, day))

    existing_forms = [LogItemForm(instance=li) for li in items_for_day]
    new_form = LogItemForm()
    return render(request, 'log/log_list.html', {'new_form': new_form, 'existing_forms': existing_forms, 'date': (year, month, day)})

def handle_post(request, date=None):
    print(request.POST)
    if 'delete_item' in request.POST:
        post = get_object_or_404(LogItem, pk=request.POST['delete_item'])
        post.delete()
        return

    if 'update_item' in request.POST:
        post = get_object_or_404(LogItem, pk=request.POST['update_item'])
        form = LogItemForm(request.POST, instance=post)
    else :
        form = LogItemForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        if date:
            year, month, day = date
            post.event_date = datetime.date(year, month, day)
        post.save()