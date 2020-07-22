from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('about_us/', views.about_us, name='about_us'),
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('my_account/', views.my_account, name='my_account'),
    path('shop/', views.shop, name='shop'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('purchases/', views.purchases, name='purchases'),
]