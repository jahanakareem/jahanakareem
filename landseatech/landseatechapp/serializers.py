from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import Brand, Category, Image, Product

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

