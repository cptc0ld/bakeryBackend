from django.db import models

# Create your models here.
from account.models import Account
from products.models import Products


class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    orderDate = models.DateTimeField(auto_now_add=True)
