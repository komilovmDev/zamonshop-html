from django.urls import path, include

from .views import savat
app_name = "orders"

urlpatterns = [
    path('', savat, name="savat"),
]

