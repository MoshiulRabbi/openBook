from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cart, Product
from django.urls import reverse

# Create your views here.
def productList(request):
    products = Product.objects.all()
    return render(request,"ecom/products.html",{"products":products})

def orderItem(request,pk):
    item = Product.objects.get(pk=pk)
    return render(request,"ecom/orderItem.html",{"item":item})


def cartList(request):
    c = Cart.objects.all()
    return render(request,"ecom/cart.html",{"c":c})


def addToCart(request,pk):
    product = Product.objects.get(pk=pk)
    cartItem = Cart(orderedProduct = product)
    cartItem.save()
    return HttpResponseRedirect(reverse("cart"))
