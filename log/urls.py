from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<int:month>/<int:day>/', views.log_day, name='log_day'),
    path('todo', views.todo, name='todo'),
    path('done_todos', views.done_todos, name='done_todos'),
    path('export', views.csv_export, name='csv_export'),
    path('search', views.search, name='search'),
    path('helm', views.helm, name='helm'),
    path('log_all', views.log_list, name='log_list'),
    path('missions', views.mission_control, name='mission_control'),
]