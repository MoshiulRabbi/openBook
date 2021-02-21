from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="home"),
    path('login',views.login_view,name="login"),
    path("logout", views.logout_view, name="logout"),
    path("donatebook", views.donatebook_view, name="donatebook"),
    path("viewbook", views.view_book, name="viewbook"),
    path("register",views.register, name="register"),
]