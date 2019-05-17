from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<int:month>/<int:day>/', views.log_day, name='log_day'),
    path('export', views.csv_export, name='csv_export'),
    path('search', views.search, name='search'),
]