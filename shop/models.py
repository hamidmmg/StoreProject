from dataclasses import field, fields

from django.db import models
from django.contrib.auth.models import User


class ItemModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.IntegerField(blank=False, null=True)
    count = models.IntegerField(null=False,default=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    body = models.CharField(max_length=600, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ItemModel = models.ForeignKey(ItemModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.i


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    #
    # def __str__(self):
    #     return str(self.item)+str(self.count)
