from django.shortcuts import render

def log_list(request):
    return render(request, 'log/log_list.html', {})