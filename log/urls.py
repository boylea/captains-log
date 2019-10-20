from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<int:month>/<int:day>/', views.log_day, name='log_day'),
    path('todo', views.todo, name='todo'),
    path('todo_done/<int:pk>', views.todo_done, name='todo_done'),
    path('export', views.csv_export, name='csv_export'),
    path('search', views.search, name='search'),
]