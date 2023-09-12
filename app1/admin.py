from django.contrib import admin
from app1.models import Userregister,Category,Product,Contactus,Order
# Register your models here.

class Userdisplay(admin.ModelAdmin):
    list_display=['name','email','number','address']
    list_filter=['name','email','number','address']
    search_fields=['name','number']

admin.site.register(Userregister,Userdisplay)
admin.site.register(Category)

class Productdisplay(admin.ModelAdmin):
    list_display=['Name','Quantity','Pricee','Description','ImageFile']
    list_filter=['Name','Description']
    search_fields=['Name']
admin.site.register(Product,Productdisplay) 

class Contactus_display(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'number','message' ]
    list_filter = ['name', 'surname', 'email' ]
    search_fields = ['name', 'email']
admin.site.register(Contactus,Contactus_display)

class Order_display(admin.ModelAdmin):
    list_display=['userid','productid','price','datetime']
admin.site.register(Order,Order_display)