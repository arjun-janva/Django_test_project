from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Category,Product,Userregister

# Create your views here.
def data(request):
    return HttpResponse("<h1>This is my first web page...</h1>")

def index(request):
    a = Category.objects.all()
    return render(request,"index.html",{'data':a})

def productall(request):
    a = Product.objects.all()
    return render(request,'product.html',{'data':a})

def productfilter(request,id):
    a = Product.objects.filter(Category=id)
    return render(request,'product.html',{'data':a})

def product_details(request,id):
    a = Product.objects.get(id=id)
    return render(request,'product_details.html',{'data':a})

def register(request):
    return render(request,'register.html') 

def login(request):
    return render(request,'login.html')

