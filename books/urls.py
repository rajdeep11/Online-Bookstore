from django.urls import path
from . import views

urlpatterns=[
    # Basic
    path("",views.home, name='home'),
    path("register/", views.register, name='register'),
    path("login/", views.login, name='login'),

    # For Customers
    path("book_list/", views.Users, name='book_list'),
    path("book_request/", views.book_request, name="book_request"),
    path("cart_checkout/", views.checkout, name="cart_checkout"),
    
]