from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required(login_url='login')
def home_view(request):
    return render(request,"home.html")




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html") 


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "register.html")



@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))




@login_required(login_url='login')
@csrf_exempt
def donatebook_view(request):
    if request.method == 'POST':

        bookname = request.POST["bookname"]
        author = request.POST["author"]
        status = "A"
        b = Book(name=bookname,author=author,user=request.user,status=status)
        b.save()
        return render(request,"donatebook.html",{
            "message": "added book"
        })
    else:
        return render(request,"donatebook.html")





#All the Book Donated By all the User
@login_required(login_url='login')
def view_book(request):
    books = Book.objects.filter(status="A")
    return render(request, "allbook.html", {'books': books})





#User Profile that shows total donated BOOK
@login_required(login_url='login')
def profile(request):
    donatedbook = Book.objects.filter(user=request.user)

    lb = lend.objects.filter(user=request.user)


    return render(request, 'profile.html', {'donatedbook': donatedbook,'lb':lb})




#Single Book Details
@login_required(login_url='login')
def book_details(request, book_id):
    b = Book.objects.get(pk=book_id)
    return render(request,"bookdetails.html", {"b":b})


#lend Book
@login_required(login_url='login')
def lend_view(request, book_id):
    b = Book.objects.get(pk=book_id)
    b.status = "B"
    b.save()
    nb = Book.objects.get(pk=book_id)
    lb = lend(book=nb,user=request.user)
    lb.save()

    return render(request, "success.html")


#return lended book

@login_required(login_url='login')
def return_book(request, book_id,lbbook_id):
    b = Book.objects.get(pk=book_id)
    b.status = "A"
    b.save()
    lb = lend.objects.get(pk=lbbook_id)
    lb.delete()

    return render(request, "success.html")