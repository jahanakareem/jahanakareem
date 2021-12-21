from typing import Generic
from django.http import request
from rest_framework import generics, serializers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from landseatechapp.models import Brand, Category, Image, Product
from .serializers import BrandSerializer, CategorySerializer, ImageSerializer, ProductSerializer, ProductimageSerializer

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


