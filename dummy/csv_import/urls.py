from django.urls import path

from . views import IndexView, index

from csv_import import views

app_name = 'csv_import'

urlpatterns = [
    path('', IndexView.as_view()),
    path('guardar', views.index, name="guardar"),
    
]
