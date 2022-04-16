from unittest import TestResult
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import Blog, Blogcategory, Blogsdetails,Brand,Jobresponsibilities, Careers, Category, Department, Education, Image, Jobtype, Location, Pdt_subdescription , Product, Services, Tdi_product
#-----------------------------Brand----------------------------------
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


#-----------------------------Category-------------------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields  = '__all__'

#-----------------------------Product---------------------------------
class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField('get_brandname')
    category_name = serializers.SerializerMethodField('get_catname')
    class Meta:
        model = Product
        fields = ('id','product_name','brand_name','category_name','category','brand','desc','title_img','created_on','updated_on')
    def get_brandname(self,obj):
        return obj.brand.brand_name
    def get_catname(self,obj):
        return obj.category.cat_name
#------------------------------Image---------------------------------
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('small','big','medium')


#-----------------------------------Productimage----------------------


class ProductimageSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField('get_brandname')
    category_name = serializers.SerializerMethodField('get_catname')
    images = ImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id','product_name','category','brand','desc','title_img','created_on','updated_on','images','brand_name','category_name')
    def create(self, validated_data):
    
        images = validated_data.pop('images')
        pdt_obj = Product.objects.create(**validated_data)


        for i in images:

            pdt_img = Image.objects.create(pdt_id=pdt_obj,small=i['small'],big=i['big'],medium=i['medium'])
            return pdt_img

    def get_brandname(self,obj):
        return obj.brand.brand_name
    def get_catname(self,obj):
        return obj.category.cat_name


class Pdt_subdescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdt_subdescription
        fields = ('id','sub_title','subdesc','imag_url','vedio_url')


class Tdi_productmageSerializer(serializers.ModelSerializer):
    tdiproduct = Pdt_subdescriptionSerializer(many=True)
    class Meta:
        model = Tdi_product
        fields = ('id','pdt_name','specifications','desc','title','image','tdiproduct')


class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class JobtypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jobtype
        fields = '__all__'

class JobresponsibilitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jobresponsibilities
        fields = '__all__'

class CareersSerializer(serializers.ModelSerializer):
    careers = JobresponsibilitiesSerializer(many=True)
    dept = serializers.SerializerMethodField('get_department')
    edu = serializers.SerializerMethodField('get_education')
    jobloc = serializers.SerializerMethodField('get_joblocation')
    jobtyp = serializers.SerializerMethodField('get_jobtype')
    
    class Meta:
        model = Careers
        fields = ('id','jobname','dept','edu','jobloc','jobtyp','jobexperience','jobdescription','createdby','updatedby','careers')
        
    def get_department(self,obj):
        return obj.department.department

    def get_education(self,obj):
        return obj.education.education

    def get_joblocation(self,obj):
        return obj.joblocation.location

    def get_jobtype(self,obj):
        return obj.jobtype.jobtype

class BlogcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Blogcategory
        fields = ('id','name')

class BlogsdetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blogsdetails
        fields = ('img','desc')

class BlogsSerializer(serializers.ModelSerializer):
    blog = BlogsdetailsSerializer(many=True)
    blogcat = serializers.SerializerMethodField('get_blogcat')
    
    class Meta:
        model = Blog
        fields = ('id','title','img','date','desc','blogcat_id','blogcat','blog')
    
    def get_blogcat(self,obj):
        return obj.blogcat_id.name
