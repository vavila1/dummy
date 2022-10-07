from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from csv_import.forms import CSV_Form

# Create your views here.

def handle_uploaded_file(f):  
    with open('csv_import/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  


class IndexView(TemplateView):
    template_name = "csv_import/index.html"

def index(request):
        if request.method == 'POST':
            csv_import = CSV_Form(request.POST, request.FILES)
            if csv_import.is_valid():
                handle_uploaded_file(request.FILES['file'])
                return HttpResponse("File uploaded successfuly")  
            else:
                csv_import = CSV_Form()
                return render(request,'index.html',{'form':csv_import})
