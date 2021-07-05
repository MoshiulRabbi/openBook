from django.urls import path
from . import views

urlpatterns = [
    path('',views.productList,name="ecommerce"),
    path('product/<int:pk>',views.orderItem,name="orderItem"),
    path('addToCart/<int:pk>',views.addToCart,name="addToCart"),
    path('cart/',views.cartList,name="cart"),
]