from django.shortcuts import render

from products.models import Category, Subcategory

# Create your views here.

def index(request):

    categories = Subcategory.objects.filter(children=None)

    context = {
        "categories": categories
    }

    return render(request, 'home/index.html', context)
    
    