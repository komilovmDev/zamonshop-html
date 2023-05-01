from django.shortcuts import render

# Create your views here.

def savat(request):
    return render(request, 'orders/savat.html')

    