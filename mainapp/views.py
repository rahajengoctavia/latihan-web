from django.shortcuts import render
from .models import *
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

def home(request):
    return render(request, 'home.html')

def shop_makeover_list(request):
    try:    
        print(request.GET)
        category_eyes = Category.objects.get(pk=1)
        product_makeup = Product.objects.filter(category=category_eyes)
        return render(request, 'shop_makeover_list.html', {'product_list': product_makeup})
    except:
        return HttpResponse("Terjadi Error")