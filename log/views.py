from django.shortcuts import render, get_object_or_404
from .models import LogItem
from .forms import LogItemForm
from django.shortcuts import redirect

def log_list(request):
    print(request)
    if request.method == "POST":
        print(request.POST)
        if 'delete_item' in request.POST:
            post = get_object_or_404(LogItem, pk=request.POST['delete_item'])
            post.delete()
            return redirect('log_list')

        if 'update_item' in request.POST:
            post = get_object_or_404(LogItem, pk=request.POST['update_item'])
            form = LogItemForm(request.POST, instance=post)
        else :
            form = LogItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('log_list')
    else:
        log_items = LogItem.objects.all();
        existing_forms = [LogItemForm(instance=li) for li in log_items]
        new_form = LogItemForm()
        return render(request, 'log/log_list.html', {'new_form': new_form, 'existing_forms': existing_forms})

