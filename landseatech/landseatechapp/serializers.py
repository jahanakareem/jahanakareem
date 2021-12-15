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
    class Meta:
        model = Product
        fields = ('id','product_name','category','brand','desc','title_img','created_by','updated_by')

#------------------------------Image---------------------------------
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

#-----------------------------------Productimage----------------------


class ProductimageSerializer(serializers.ModelSerializer):
    img_id=ProductSerializer()
    class Meta:
        model = Image
        fields = ('id','img_id','small','big','medium','created_by','updated_by')
    def create(self, validated_data,images):
        print(images)
        items = validated_data.pop('img_id')
        pdt_obj = Product.objects.create(**items)
        #pdt_img = Image.objects.create(img_id=pdt_obj)

        for i in images:

            pdt_img = Image.objects.create(img_id=pdt_obj,small=i['small'],big=i['big'],medium=i['medium'])
            pdt_img.save()
    
# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = '__all__'   abnaaa



