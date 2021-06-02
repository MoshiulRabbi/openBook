from openbook.views import profile
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product

# Create your views here.
def productList(request):
    products = Product.objects.all()
    return render(request,"ecom/products.html",{"products":products})