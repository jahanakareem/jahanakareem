import base64

import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from email.mime.base import MIMEBase
from email import encoders, message
from asyncio import streams
from typing import Generic
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse, request
from rest_framework import generics, serializers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from .models import Blog, Blogcategory, Brand, Careers, Category, Department, Image, Product, Tdi_product,Services
from .serializers import BlogcategorySerializer, BlogsSerializer, DepartmentSerializer, ServicesSerializer,BrandSerializer, CareersSerializer, CategorySerializer, ImageSerializer, ProductSerializer, ProductimageSerializer, Tdi_productmageSerializer
from django.core.mail import send_mail


# Create your views here.
#-----------------------------Brand---------------------------------------
class Addbrand(generics.CreateAPIView):
    serializer_class = BrandSerializer

    def post(self, request):
        duplicate = Brand.objects.filter(
            brand_name__icontains=request.data['brand_name']).count()
        if duplicate > 0:
            return Response("Already Existing Brand ")
        else:
            serializer = BrandSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("added successfully")
            return Response("failed")


class Listbrand(generics.GenericAPIView):
    serializer_class = BrandSerializer

    def get(self,request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset,many=True)
        return Response(serializer.data)

class Updatebrand(generics.GenericAPIView):
    serializer_class = BrandSerializer
    def put(self,request,pk):
        queryset = Brand.objects.get(id=pk)
        serializer = BrandSerializer(instance=queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("updated")

#-----------------------------Category---------------------------------------

class Addcategory(generics.CreateAPIView):
    serializer_class = CategorySerializer

    def post(self, request):
        duplicate = Category.objects.filter(
            cat_name__icontains=request.data['cat_name']).count()
        if duplicate>0:
            return Response("category already exists")
        else:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("category added successfully")
            return Response("failed")

class Listcategory(generics.GenericAPIView):
    serializer_class = CategorySerializer

    def get(self,request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset,many=True)
        return Response(serializer.data)


class Updatecategory(generics.GenericAPIView):
    serializer_class = CategorySerializer
    def put(self,request,pk):
        queryset = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("updated")

#----------------------------------Productimage------------------------------

class Addproductsandimages(generics.CreateAPIView):
       
    serializer_class = ProductimageSerializer
    model = Image
    

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=self.request.data)
        print(serializer)
        images = self.request.data['images']
        print(images)
        if serializer.is_valid():
            # print(serializer.validated_data)
            # print('#####################')
            images_obj = ProductimageSerializer.create(
                self, serializer.validated_data, images)
            img = ProductimageSerializer(images_obj).data
            return Response({"status": True, "response": {}})
        # return Response(leadcategory_obj)
        return Response({"status": False, "response": {}})



class Listpdtimages(generics.GenericAPIView):
    serializer_class = ProductimageSerializer

    def get(self,request):
        queryset = Product.objects.all()
        serializer = ProductimageSerializer(queryset,many=True)
        return Response(serializer.data)

#--------------------------------------------------------------------

class Listpdtimagesbyid(generics.GenericAPIView):
    serializer_class = ImageSerializer

    def get(self,request,pk):
        queryset = Image.objects.filter(pdt_id=pk)
        serializer = ImageSerializer(queryset,many=True)
        return Response(serializer.data)


class Listproduct(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def get(self,request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data)


class Listproductbybrandid(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def get(self,request,pk):
        queryset = Product.objects.filter(brand=pk)
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data)



class Listproductbycategoryid(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def get(self,request,pk):
        queryset = Product.objects.filter(category=pk)
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data)


class Listproductdetailbyid(generics.GenericAPIView):
    serializer_class = ProductimageSerializer
    def get(self,request,pk):
        queryset = Product.objects.filter(id=pk)
        print(queryset)
        serializer = ProductimageSerializer(queryset,many=True)
        return Response(serializer.data)

class setPagination(PageNumberPagination):
    page_size=2

class PaginationAPi(ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    pagination_class = setPagination


class Listtdiproducts(generics.GenericAPIView):
    serializer_class = Tdi_productmageSerializer

    def get(self,request):
        queryset = Tdi_product.objects.all()
        serializer = Tdi_productmageSerializer(queryset,many=True)
        return Response(serializer.data)


class Listtdiproductsbyid(generics.GenericAPIView):
    serializer_class = Tdi_productmageSerializer

    def get(self,request,x):
        queryset = Tdi_product.objects.filter(id=x)
        serializer = Tdi_productmageSerializer(queryset,many=True)
        return Response(serializer.data)

class Emailsend(generics.CreateAPIView):
    def post(self,request):
        name = request.data['name']
        email = request.data['email']
        number = request.data['number']
        cmpny_address = request.data['cmpny_address']
        message = request.data['message']
        product = request.data['product']
        data ={
            'mailsubject':"Request for Quote - "+product,
            'name': name,
            'email':email,
            'number':number,
            'cmpny_address':cmpny_address,
            'message':message,
            'product':product        
        }
        message = '''
             <h3> Name:{} </h3><br> 
             <h3> From:{} </h3><br> 
             <h3> Mobile:{} </h3><br> 
             <h3> Company Address:{} </h3><br> 
             <h3> New message:{} </h3><br> 
             <h3> Product:{} </h3><br> 
        '''.format(data['name'],data['message'],data['email'],data['cmpny_address'],data['number'],data['product'])
        # send_mail(data['mailsubject'],message,'',['abnajahana@gmail.com'])
        email = EmailMessage(data['mailsubject'],message,'landseatechweb@gmail.com',['sales@landseatech.co.uk'])
        email.content_subtype='html'
        email.send()
        return Response("mail is sent")


class Categorymailsend(generics.CreateAPIView):
    def post(self,request):
        name = request.data['name']
        email = request.data['email']
        number = request.data['number']
        cmpny_address = request.data['cmpny_address']
        message = request.data['message']
        category = request.data['category']
        data ={
            'mailsubject':"Request for Quote - "+category,
            'name': name,
            'email':email,
            'number':number,
            'cmpny_address':cmpny_address,
            'message':message,
            'category':category        
        }
        print(data)
        message = '''
             <h3> Name:{} </h3><br> 
             <h3> From:{} </h3><br> 
             <h3> Mobile:{} </h3><br> 
             <h3> Company Address:{} </h3><br> 
             <h3> New message:{} </h3><br> 
             <h3> Category:{} </h3><br> 
        '''.format(data['name'],data['message'],data['email'],data['cmpny_address'],data['number'],data['category'])
        # send_mail(data['mailsubject'],message,'',['abnajahana@gmail.com'])
        email = EmailMessage(data['mailsubject'],message,'landseatechweb@gmail.com',['sales@landseatech.co.uk'])
        email.content_subtype='html'
        email.send()
        return Response("Category mail is sent")

class Filesend(generics.CreateAPIView):
    def post(self,request):
            name = request.data['name']
            mail = request.data['mail']
            jobname = request.data['jobname']
            print(jobname)
            mail_id = 'sales@landseatech.co.uk'
            data ={
            'mailsubject':'{} {}'.format(jobname,name),
            'name': name,
            'email':mail ,
            }
            
            message='''<h3> Name: {} </h3></br>
                       <h3> Email: {} </h3>
            '''.format(data['name'],data['email'])
            email = EmailMessage(data['mailsubject'],message,'landseatechweb@gmail.com',[mail_id])
            email.content_subtype='html'
            file = request.data['file']
            email.attach(file.name,file.read(), file.content_type)
            # send_mail(subject,message,'',['abnajahana@gmail.com'])
            email.send()
            return Response("sent")


class contactEmailsend(generics.CreateAPIView):
    def post(self,request):

        name = request.data['name']
        email = request.data['email']
        number = request.data['number']
        subject = request.data['subject']
        message  =request.data['message']
        data ={
            'mailsubject':"Request for Contact - " +subject,
            'name': name,
            'email':email,
            'number':number,
            'subject':subject,
            'message':message        
        }
        message = '''
            <h3> Subject:{} </h3>
            <h3> Name:{} </h3>
            <h3> From:{} </h3>
            <h3> Mobile:{} </h3>
            <h3> Message:{} </h3>
        '''.format(data['subject'],data['name'],data['email'],data['number'],data['message'])
        # send_mail(data['mailsubject'],message,'',['abnajahana@gmail.com'])
        email = EmailMessage(data['mailsubject'],message,'landseatechweb@gmail.com',['sales@landseatech.co.uk'])
        email.content_subtype='html'
        email.send()
        return Response("Contact Form sent")
  
        
class Listservices(generics.GenericAPIView):
    serializer_class = ServicesSerializer

    def get(self,request):
        queryset = Services.objects.all()
        serializer = ServicesSerializer(queryset,many=True)
        return Response(serializer.data)


class Listcareers(generics.GenericAPIView):
    serializer_class = CareersSerializer

    def get(self,request):
        queryset = Careers.objects.all()
        serializer = CareersSerializer(queryset,many=True)
        return Response(serializer.data)

class Listblog(generics.GenericAPIView):
    serializer_class = BlogsSerializer

    def get(self,request):
        queryset = Blog.objects.all() 
        serializer = BlogsSerializer(queryset,many=True)
        return Response(serializer.data)

class Listcareersbyid(generics.GenericAPIView):
    serializer_class = CareersSerializer
    def get(self,request,pk):
        queryset = Careers.objects.filter(id=pk)
        print(queryset)
        serializer = CareersSerializer(queryset,many=True)
        return Response(serializer.data)

class Listblogbyid(generics.GenericAPIView):
    serializer_class = BlogsSerializer
    def get(self,request,pk):
        queryset = Blog.objects.filter(id=pk)
        print(queryset)
        serializer = BlogsSerializer(queryset,many=True)
        return Response(serializer.data)


class Listblogbycategory(generics.GenericAPIView):
    serializer_class = BlogsSerializer
    def get(self,request,pk):
        queryset = Blog.objects.filter(blogcat_id=pk)
        print(queryset)
        serializer = BlogsSerializer(queryset,many=True)
        return Response(serializer.data)


class Listdepartment(generics.GenericAPIView):
    serializer_class = DepartmentSerializer

    def get(self,request):
        queryset = Department.objects.all()
        serializer = DepartmentSerializer(queryset,many=True)
        return Response(serializer.data)


class Listblogcategory(generics.GenericAPIView):
    serializer_class = BlogcategorySerializer

    def get(self,request):
        queryset = Blogcategory.objects.all()
        serializer = BlogcategorySerializer(queryset,many=True)
        return Response(serializer.data)


class Listcareerbydepartment(generics.GenericAPIView):
    serializer_class = CategorySerializer
    def get(self,request,pk):
        queryset = Careers.objects.filter(department=pk)
        print(queryset)
        serializer = CareersSerializer(queryset,many=True)
        return Response(serializer.data)

