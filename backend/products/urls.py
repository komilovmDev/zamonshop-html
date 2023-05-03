from django.urls import path, include

from .views import index, products ,product
app_name = "products"




urlpatterns = [
    path('products/', products, name="products"),
    path('products/', product, name="product"),
]

