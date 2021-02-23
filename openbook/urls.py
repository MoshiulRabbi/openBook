from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="home"),
    path('login',views.login_view,name="login"),
    path("logout", views.logout_view, name="logout"),
    path("donatebook", views.donatebook_view, name="donatebook"),
    path("viewbook", views.view_book, name="viewbook"),
    path("register",views.register, name="register"),
    path('profile/',views.profile, name="profile"),
    path('viewbook/<int:book_id>', views.book_details,name="book_details"),
    path('lend/<int:book_id>', views.lend_view,name="lend"),
    path('returnbook/<int:book_id>/<int:lbbook_id>', views.return_book,name="returnbook")
]

# url(r'^profile/(?P<username>\w+)/$',profile,name='profile'),

# path('<str:username>/',views.profile, name="profile"),