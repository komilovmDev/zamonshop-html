from products.models import Category, Subcategory

def categories(request):
    return Subcategory.objects.filter(children=None)
    