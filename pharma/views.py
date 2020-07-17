from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def home(request):

    return render(request, 'home.html')

def about_us(request):

    return render(request, 'about_us.html')

def blog(request):

    return render(request, 'blog.html')

def cart(request):

    return render(request, 'cart.html')

def checkout(request):

    return render(request, 'checkout.html')

def contact(request):

    return render(request, 'contact.html')

def login_register(request):

    return render(request, 'login_register.html')

def my_account(request):

    return render(request, 'my_account.html')

def shop(request):

    return render(request, 'shop.html')

def wishlist(request):

    return render(request, 'wishlist.html')