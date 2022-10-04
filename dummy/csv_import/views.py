from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    pass

class IndexView(TemplateView):
    template_name = "csv_import/index.html"

