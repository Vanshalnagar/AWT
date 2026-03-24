from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1> Aayush Shah</h1>")

def aboutpage(request):
    return render(request,'home.html')