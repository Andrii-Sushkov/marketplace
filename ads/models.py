from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    title = models.CharField(max_length=30)
    detail = models.TextField(blank=True)
    image = models.ImageField(upload_to='create/')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)