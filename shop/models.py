from django.db import models
from django.contrib.auth.models import User


class ItemModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    body = models.CharField(max_length=600, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ItemModel = models.ForeignKey(ItemModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title