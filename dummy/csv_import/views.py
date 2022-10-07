from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from csv_import.forms import CSV_Form
from csv_import.models import Estudiante

# Create your views here.

def handle_uploaded_file(f):  
    with open('csv_import/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    arr = []
    with open('csv_import/static/upload/'+f.name) as archivo:
        for linea in archivo:
            s = linea.split(',')
            s[1] = s[1].rstrip()
            arr.append(s)
    return arr

def insertar_algo(arr):
    for i in arr:
        estudiante = Estudiante()
        estudiante.nombre = i[0]
        estudiante.matricula = i[1]
        estudiante.save()
    

class IndexView(TemplateView):
    template_name = "csv_import/index.html"

def index(request):
        if request.method == 'POST':
            csv_import = CSV_Form(request.POST, request.FILES)
            if csv_import.is_valid():
                arr = handle_uploaded_file(request.FILES['file'])
                insertar_algo(arr)
                return HttpResponse(arr)  
            else:
                csv_import = CSV_Form()
                return render(request,'index.html',{'form':csv_import})
