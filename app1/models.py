from django.db import models

# Create your models here.
class Userregister(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20,default=' ')
    email = models.EmailField(max_length=200)
    number = models.IntegerField()
    address=models.TextField(max_length=250)
    password=models.CharField(max_length=12)

    def __str__(self) -> str:
        return  str(self.name) + " " + str(self.email)

class Category(models.Model):
    Category_name = models.CharField(max_length=20)
    ImageFile = models.ImageField(upload_to='category_image',blank=True)
    def __str__(self) -> str:
        return self.Category_name
    
class Product(models.Model):
    Category = models.ForeignKey('Category',on_delete=models.CASCADE)
    Name = models.CharField(max_length=25)
    ImageFile = models.ImageField(upload_to='product_image',blank=True)
    Quantity = models.IntegerField(default=1)
    Pricee = models.IntegerField(default=0)
    Description = models.TextField(max_length=100,default=" ")
    def __str__(self) -> str:
        return self.Name

class Contactus(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    number = models.IntegerField()
    message=models.TextField(max_length=250)
    def __str__(self) ->str:
        return str(self.name) + " " + str(self.surname)+ " " + str(self.email)+" "+ str(self.message)

class Profile(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20,default=' ')
    email = models.EmailField(max_length=200)
    number = models.IntegerField()
    address=models.TextField(max_length=250)
    password=models.CharField(max_length=12)

    def __str__(self) -> str:
        return  str(self.name) + " " + str(self.email)
    
class Order(models.Model):
    userid = models.CharField(max_length=200)
    productid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    Quantity = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    datetime= models.DateTimeField(auto_created=True,auto_now=True)
    paymentmethod = models.CharField(max_length=200)
    transactionid = models.CharField(max_length=200)