from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('my_account/', views.my_account, name='my_account'),
    path('shop/', views.shop, name='shop'),
    path('wishlist/', views.wishlist, name='wishlist'),
]