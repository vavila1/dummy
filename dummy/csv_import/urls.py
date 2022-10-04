from django.urls import path

from . import views

app_name = 'csv_import'

urlpatterns = [
    path('', views.index, name='index'),
    
]
