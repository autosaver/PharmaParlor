from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    location = models.CharField(max_length=60, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

    def update_profile(self, using=None, fields=None, **kwargs):
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_profile(self):
        self.delete()

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
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategory')

    def __str__(self):
        return self.name


class SubSubCategory(models.Model):
    name = models.CharField(max_length=250, blank=True)
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name='subsubctegory')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, blank=True)
    subsubcategory = models.ForeignKey(
        SubSubCategory, on_delete=models.CASCADE, related_name='product')
    description = models.CharField(max_length=250, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    discountedprice = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True)
    image = models.ImageField(upload_to='products/',
                              blank=True, default=' static/img/product/product-4.jpg')

    def __str__(self):
        return self.name

    @classmethod
    def search_product(cls, name):
        return cls.objects.filter(name__icontains=name).all()

    # @classmethod
    # def get_by_id(cls, pk, **kwargs):
    #     return cls.objects.get(pk=pk)


class Order(models.Model):
    customer = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transactoin_id = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.stock >= 1:
                shipping = True

        return shipping


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    address = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)
    zipcode = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.address


class Rating(models.Model):
    rating = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),
              (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'),)
    score = models.FloatField(choices=rating, default=0, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='rater')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='ratings', null=True)

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
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Product'

    class Meta:
        ordering = ["-pk"]
