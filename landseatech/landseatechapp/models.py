from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_image = models.FileField(upload_to='images/',null=True,blank=True)
    desc = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.brand_name

class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_type = models.CharField(max_length=100)
    cat_desc = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.cat_name

class Product(models.Model):
    
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    desc = models.TextField()
    title_img = models.FileField(upload_to='images/',null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.product_name

class Image(models.Model):
    pdt_id = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)
    small = models.FileField(upload_to='images/',null=True,blank=True)
    big = models.FileField(upload_to='images1/',null=True,blank=True)
    medium = models.FileField(upload_to='images2/',null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['id']
    
    def __str__(self):
        return str(self.pdt_id)

class Tdi_product(models.Model):
    pdt_name = models.CharField(max_length=50,null=True,blank=True)
    specifications = models.TextField(null=True,blank=True)
    title = models.CharField(max_length=50,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    image = models.FileField(upload_to='images/',default='images/no-image-avilable_yqhw4i.jpg')
    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.pdt_name


class Pdt_subdescription(models.Model):
    sub_title = models.CharField(max_length=50,null=True,blank=True)
    subdesc = models.TextField(null=True,blank=True)
    imag_url = models.FileField(upload_to='images/',null=True,blank=True)
    vedio_url = models.CharField(max_length=500,null=True,blank=True)
    tdi_product = models.ForeignKey(Tdi_product,related_name='tdiproduct',on_delete=models.CASCADE)
    class Meta:
        ordering=['id']
    
    def __str__(self):
        return str(self.id)



class Services(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    titleimage = models.FileField(upload_to='images/',null=True,blank=True)
    subicon = models.FileField(upload_to='images/',null=True,blank=True)
    
    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.title

class Department(models.Model):
    department = models.CharField(max_length=100)

    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.department

class Education(models.Model):
    education = models.CharField(max_length=100)

    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.education

class Location(models.Model):
    location = models.CharField(max_length=100)

    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.location

class Jobtype(models.Model):
    jobtype = models.CharField(max_length=100)

    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.jobtype

class Careers(models.Model):
    jobname = models.CharField(max_length=50,null=True,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    education = models.ForeignKey(Education,on_delete=models.CASCADE)
    joblocation = models.ForeignKey(Location,on_delete=models.CASCADE)
    jobtype = models.ForeignKey(Jobtype,on_delete=models.CASCADE)
    jobexperience = models.CharField(max_length=50,null=True,blank=True)
    jobdescription = models.TextField(null=True,blank=True)
    createdby = models.DateTimeField(auto_now_add=True)
    updatedby = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.jobname

class Jobresponsibilities(models.Model):
    career_id = models.ForeignKey(Careers,related_name='careers',on_delete=models.CASCADE)
    jobresponsibility = models.TextField(null=True,blank=True)
    
    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.jobresponsibility

class Blogcategory(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200,null=True,blank=True)
    
    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    img = models.FileField(upload_to='images/',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    blogcat_id = models.ForeignKey(Blogcategory,on_delete=models.CASCADE)


    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.title

class Blogsdetails(models.Model):
    blog_id = models.ForeignKey(Blog,related_name='blog',on_delete=models.CASCADE)
    img = models.FileField(upload_to='images/',null=True,blank=True)
    desc = models.TextField()
   
    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.desc


