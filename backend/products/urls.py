from django.urls import path, include

from .views import index, products
app_name = "products"




urlpatterns = [
    path('', index, name="home"),
    path('products/', products, name="products"),
]

