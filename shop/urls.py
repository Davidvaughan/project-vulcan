from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('category/<int:id>/', views.category_product),
    path('product/<int:id>/', views.product_detail)
]
