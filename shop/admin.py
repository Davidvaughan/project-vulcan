from django.contrib import admin

from .models import Category, Product

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'category']

admin.site.register(Product, ProductAdmin)
