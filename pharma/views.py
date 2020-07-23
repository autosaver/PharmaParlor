from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from .decorators import unauthenticated_user
import random
from .forms import *
from .models import *

# Create your views here.


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 'Account was created for' + ' ' + username)
            return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in as' + ' ' + username)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username and/or Password')

    context = {}
    return render(request, 'auth/login.html', context)


def logoutUser(request):
    logout(request)
    messages.success(
        request, 'You have logged out. Thank you for using our services.')
    return redirect('home')


def home(request):

    return render(request, 'home.html')


def shop(request):
    products = Product.objects.all()
    # product = Product.objects.get(pk=pk)
    context = {'products': products,
               'product': product}

    return render(request, 'shop.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items,
               'order': order}

    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items,
               'order': order}

    return render(request, 'checkout.html', context)


def about_us(request):

    return render(request, 'about_us.html')


def contact(request):

    return render(request, 'contact.html')


def product(request):

    return render(request, 'product_details.html')


def my_account(request):

    return render(request, 'my_account.html')


def blog(request):

    return render(request, 'blog.html')


def wishlist(request):

    return render(request, 'wishlist.html')


def dashboard(request):

    return render(request, 'admin/dashboard.html')


def purchases(request):

    return render(request, 'admin/purchases.html')
