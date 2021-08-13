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

def search(request):
    return render(request, 'search.html')

def shop_makeover_list(request):
    try:    
        print(request.GET)
        category_eyes = Category.objects.get(pk=1)
        if(request.GET=={}): 
            product_eyes = Product.objects.filter(category=category_eyes)
        else:
            product_eyes = Product.objects.filter(category=category_eyes).filter(name__contains=request.GET['product_name'])
        if(product_eyes.count() != 0):
            return render(request, 'shop_makeover_list.html', {'product_list': product_eyes, 'available': True})
        else:
            return render(request, 'shop_makeover_list.html', {'available': False})
    except:
        return HttpResponse("Terjadi Error")