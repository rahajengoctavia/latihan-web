from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def landing_page(request):
    return HttpResponse("Hello, world")

def second_page(request):
    return HttpResponse("Secondpage")

def example(request):
    return render(request, 'example.html')

def newpage(request):
    return HttpResponse("new")

def a(request):
    return HttpResponse()
