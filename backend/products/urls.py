from django.urls import path, include

from .views import index, products
app_name = "products"




urlpatterns = [
    path('products/', products, name="products"),
]

