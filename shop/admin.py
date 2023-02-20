from django.contrib import admin
from .models import ItemModel, Comment, User

admin.site.register(ItemModel)
admin.site.register(Comment)
