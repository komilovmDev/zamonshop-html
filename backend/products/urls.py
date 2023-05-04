from django.urls import path, include

from .views import products ,product
app_name = "products"




urlpatterns = [
    path('products/', products, name="products"),
    path('products/', product, name="product"),
]

