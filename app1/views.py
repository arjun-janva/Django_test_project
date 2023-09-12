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
    if 'email' in request.session:
        a = Product.objects.get(id=id)
        return render(request,'product_details.html',{'data':a})
    else:
        return redirect('login')

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
            return redirect('login')
        else:
            return render(request,'register.html',{'m':'User with this email already exist'})
    return render(request,'register.html') 

def login(request):
            
    if request.method=='POST':
        email1=request.POST['email']
        password1=request.POST['password']
        try:
            user= Userregister.objects.get(email=email1,password=password1)
            if user:
                request.session['email'] = user.email
                request.session['id'] = user.pk
                return redirect('index1')
                print(request.session['email'],request.session['id'])
            else:
                return render(request,'login.html',{"m":"Invalid Credentials"})
        except:
            return render(request,'login.html',{"m":"Invalid Credentials"})
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

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        del request.session['id']
        return redirect('login')
    else:
        return redirect('login')


def profile(request):
    if 'email' in request.session:
        user=Userregister.objects.get(email=request.session['email'])
        if request.method == 'POST':
            fname1=request.POST['fname']
            sname1=request.POST['sname']
            address1=request.POST['address']
            oldpass=request.POST['oldpassword']
            newpass=request.POST['newpassword']
            number1=request.POST['number']
            user.name=fname1
            user.surname=sname1
            user.address=address1
            user.number=number1
            if oldpass=="" and newpass=="":
                user.save()
                return render(request,'profile.html',{'user':user,'m':'profile is updated..'})
            if user.password==oldpass:
                user.password=newpass
                user.save()
                return render(request,'profile.html',{'user':user,'m':'profile is updated..'})
            else:
                return render(request,'profile.html',{'user':user,'m':'Invalid oldpassword, Please enter correct password'})
        return render(request,'profile.html',{'user':user})
    else:
        return redirect('login')

# def order(request):
