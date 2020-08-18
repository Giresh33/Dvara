from django.contrib import admin

# Register your models here.
from .models import Category, Subcategory, Person

admin.site.register(Subcategory)
admin.site.register(Category)
admin.site.register(Person)