from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required(login_url = '/login')
def Users(request):
    books = Book.objects.all()
    total_books = books.count()
    return render (request, "book_list.html", {'books':books, 'total_books':total_books})

def book_request(request):
    if request.method=="POST":
        user = request.user
        book_name = request.POST['book_name']
        author = request.POST['author']
        book = Request_Book(user=user, book_name=book_name, author=author)
        book.save()
        thank = True
        return render(request, "book_request.html", {'thank':thank})
    else:
        return render(request, "book_request.html")

def login(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already Taken..!')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already Exists..!')
                return render(request, 'register.html')
            else:
                user= User.objects.create_user(
                    username= username,
                    password= password1,
                    email= email,
                    first_name= first_name,
                    last_name= last_name
                )
                user.save()
                messages.info(request,'User Created')
                return redirect(request, 'login.html')
        else:
            print('Passwords not matching...!!')

    else:
        return render(request, 'register.html')