from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

#from .template import index
# Create your views here.

def update(request):
    student = Student.objects.all 
    return HttpResponse(student)
    
#def welcome(request):
 #   return render(request, 'index.html')
    