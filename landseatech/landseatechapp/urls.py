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
    path('listtdiproducts/',Listtdiproducts.as_view()),
    path('emailsend/',Emailsend.as_view()),
    path('categorymailsend/',Categorymailsend.as_view()),
    path('contactemailsend/',contactEmailsend.as_view()),
    path('listtdiproductsbyid/<int:x>/',Listtdiproductsbyid.as_view()),
    
    path('listservices/',Listservices.as_view()),
    path('listcareers/',Listcareers.as_view()),
    path('listblog/',Listblog.as_view()),
    path('listcareersbyid/<int:pk>/',Listcareersbyid.as_view()),
    path('listblogbyid/<int:pk>/',Listblogbyid.as_view()),
    path('listblogbycategory/<int:pk>/',Listblogbycategory.as_view()),
    path('listdepartment/',Listdepartment.as_view()),
    path('listblogcategory/',Listblogcategory.as_view()),
    path('filesend/',Filesend.as_view()),
    path('listcareerbydepartment/<int:pk>/',Listcareerbydepartment.as_view())






]
