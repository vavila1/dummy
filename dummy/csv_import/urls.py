from django.urls import path

from . views import IndexView

app_name = 'csv_import'

urlpatterns = [
    path('', IndexView.as_view()),
    
]
