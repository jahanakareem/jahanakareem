from .views import *
from django.urls import path
from django.conf import settings
from rest_framework import views


urlpatterns = [
    path('addbrand/',Addbrand.as_view()),
    path('listbrand/',Listbrand.as_view()),
    path('addcategory/',Addcategory.as_view()),
    path('listcategory/',Listcategory.as_view()),
    path('addpdtimg/',Addproductsandimages.as_view()),
    path('listpdtimages/',Listpdtimages.as_view())
  
    
   
]
