from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Category

def index(request):

    return render(request, 'shop/index.html')


def category_product(request, id):

    products = Product.objects.all().filter(category=id)

    return render(request, 'shop/category_products.html', {'products' : products})


def product_detail(request, id):

    product = Product.objects.get(id=id)

    return render(request, 'shop/product_detail.html', {'product' : product})
