from django.urls import path
from app1.views import *

urlpatterns = [
    path('data/',data),
    path('',index, name='index1'),
    path('product-all/',productall),
    path('product-filter/<int:id>/',productfilter),
    path('register/',register),
    path('login/',login,name='login'),
    path('product_details/<int:id>/',product_details,name='productdetails'),
    path('contact',Contact_us)
]