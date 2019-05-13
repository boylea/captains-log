from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_list, name='log_list'),
    path('<int:year>/<int:month>/<int:day>/', views.log_day, name='log_day'),
]