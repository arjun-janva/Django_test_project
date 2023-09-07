from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import *
# from app1.models import Category,Product,Userregister,Contactus

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
    if request.method=="POST":
        fname1=request.POST['fname']
        sname1=request.POST['sname']
        email1=request.POST['email']
        address1=request.POST['address']
        password1=request.POST['password']
        number1=request.POST['number']
        user=Userregister(name=fname1,surname=sname1, email=email1,number=number1,address=address1,password=password1)
        data = Userregister.objects.filter(email=email1)
        if len(data)==0:
            user.save()
            return redirect(login)
        else:
            return render(request,'register.html',{'m':'User with this email already exist'})
    return render(request,'register.html') 

def login(request):
    if request.method=='POST':
        email1=request.POST['email']
        password1=request.POST['password']
        try:
            user=Userregister.object.get(email=email1,password=password1)
            if user:
                request.session['email'] =user.email
                request.session['id'] = user.pk
                return redirect(index1)
            else:
                return render(request,'login.html',{'m':'invalid Credentials'})
        except:
            return render(request,'login.html')
    return render(request,'login.html')

def Contact_us(request):
    if request.method=="POST":
        fname2 = request.POST['fname']
        sname2 = request.POST['sname']
        email2 = request.POST['email']
        number2 = request.POST['number']
        message2 = request.POST['message']
        userdata = Contactus(name=fname2,surname=sname2,email=email2,number=number2,message=message2)
        data = Contactus.objects.filter(email=email2)
        if len(data)==0:
            userdata.save()
        else:
            return render(request,"contact.html")

    return render(request,'contact.html')
