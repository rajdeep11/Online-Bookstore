from os import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    CATEGORY = (
        ('Mystery', 'Mystery'),
        ('Thriller', 'Thriller'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Humor', 'Humor'),
        ('Horror', 'Horror'),
        ('Mystery', 'Mystery'),
    )

    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, choices=CATEGORY)
    price = models.FloatField()
    stock = models.IntegerField(default=5)

    def __str__(self):
        return self.book_name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)    
    items_json = models.CharField(max_length=5000, blank=True)
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return str(self.user)

class Request_Book