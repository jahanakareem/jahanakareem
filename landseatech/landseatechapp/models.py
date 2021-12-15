
from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    created_by = models.DateTimeField(auto_now=True)
    updated_by = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.brand_name

class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_type = models.CharField(max_length=100)
    created_by = models.DateTimeField(auto_now=True)
    updated_by = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.cat_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    desc = models.CharField(max_length=500)
    title_img = models.FileField(upload_to='images/',null=True,blank=True)
    created_by = models.DateTimeField(auto_now=True)
    updated_by = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.product_name

class Image(models.Model):
    img_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    small = models.FileField(upload_to='images/',null=True,blank=True)
    big = models.FileField(upload_to='images1/',null=True,blank=True)
    medium = models.FileField(upload_to='images2/',null=True,blank=True)
    created_by = models.DateTimeField(auto_now=True)
    updated_by = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['id']
    
    def __str__(self):
        return str(self.img_id)


