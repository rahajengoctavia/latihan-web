from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def landing_page(request):
    return HttpResponse("Hello, world")

def example(request):
    return render(request, 'example.html')

def newpage(request):
    return HttpResponse("new")

def a(request):
    return HttpResponse()

def shop(request):
    return render(request, 'shop.html')

def first_page(request):
    return render(request, 'firstpage.html')

def second_page(request):
    return render(request, 'secondpage.html')

def makeover(request):
    return render(request, 'makeover.html')

