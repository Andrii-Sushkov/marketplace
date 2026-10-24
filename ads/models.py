from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Ad(models.Model):
    title = models.CharField(max_length=30)
    detail = models.TextField(blank=True)
    image = models.ImageField(upload_to='create/')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='item')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)