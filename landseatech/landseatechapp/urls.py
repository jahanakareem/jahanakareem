from .views import *
from django.urls import path
from django.conf import settings
from rest_framework import views


urlpatterns = [
    path('addbrand/',Addbrand.as_view()),
    path('listbrand/',Listbrand.as_view()),
    # path('updatebrand/<int:pk>/',Updatebrand.as_view()),
    # path('addcategory/',Addcategory.as_view()),
    path('listcategory/',Listcategory.as_view()),
    # path('updatecategory/<int:pk>/',Updatecategory.as_view()),
    path('addpdtimg/',Addproductsandimages.as_view()),
    path('listpdtimages/',Listpdtimages.as_view()),
    # path('listproduct/',Listproduct.as_view()),
    # path('listpdtimagesbyid/<int:pk>/',Listpdtimagesbyid.as_view()),
    path('listproductbybrand/<int:pk>/',Listproductbybrandid.as_view()),
    path('listproductbycategory/<int:pk>/',Listproductbycategoryid.as_view()),
    path('listproductdetail/<int:pk>/',Listproductdetailbyid.as_view()),
    path('PaginationAPi',PaginationAPi.as_view()),

  
    
   
]
