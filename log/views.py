from django.shortcuts import render
from .models import LogItem
from .forms import LogItemForm
from django.shortcuts import redirect

def log_list(request):
    print(request)
    if request.method == "POST":
        form = LogItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('log_list')
    else:
        log_items = LogItem.objects.all();
        form = LogItemForm()
        return render(request, 'log/log_list.html', {'log_items': log_items, 'form': form})

