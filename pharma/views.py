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
import random
from .forms import *
from .models import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created successfully!, You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form':form})


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

def product(request):

    return render( request, 'product_details.html')

def my_account(request):

    return render(request, 'my_account.html')

def shop(request):

    return render(request, 'shop.html')

def wishlist(request):

    return render(request, 'wishlist.html')

def dashboard(request):

    return render(request, 'admin/dashboard.html')

def purchases(request):

    return render(request, 'admin/purchases.html')