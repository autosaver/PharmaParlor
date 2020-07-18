from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Category(models.Model):
    name = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=250, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')

    def __str__(self):
        return self.name

class SubSubCategory(models.Model):
    name = models.CharField(max_length=250, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subsubctegory')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250, blank=True)
    subsubcategory = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE, related_name='product')
    description = models.CharField(max_length=250, blank=True)
    price = models.IntegerField(blank=True)
    discountedprice = models.IntegerField(blank=True)
    stock = models.IntegerField( blank=True)
    image = models.ImageField(upload_to='products/', blank=True, default='default.png')

    def __str__(self):
        return self.name

    @classmethod
    def search_product(cls, name):
        return cls.objects.filter(name__icontains=name).all()

class Order(models.Model):
    pass

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    pass

    def __str__(self):
        return self.name

class Rating(models.Model):
    rating = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),)
    score = models.FloatField(choices=rating, default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(product_id=id).all()
        return ratings

    def __str__(self):
        return self.name

class Review(models.Model):
    review = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Product'
    
    class Meta:
        ordering = ["-pk"]