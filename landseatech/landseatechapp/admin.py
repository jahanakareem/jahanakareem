from django.contrib import admin

from .models import Blogcategory, Blog, Blogsdetails,Brand, Careers, Category, Department, Education, Image, Jobresponsibilities, Jobtype, Location, Pdt_subdescription, Product, Services, Tdi_product

# Register your models here.
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Tdi_product)
admin.site.register(Pdt_subdescription)
admin.site.register(Department)
admin.site.register(Education)
admin.site.register(Location)
admin.site.register(Jobtype)
admin.site.register(Careers)
admin.site.register(Jobresponsibilities)
admin.site.register(Blogcategory)
admin.site.register(Blogsdetails)
admin.site.register(Blog)
admin.site.register(Services)

