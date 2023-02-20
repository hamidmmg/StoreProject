from django.contrib import admin
from .models import ItemModel, Comment, Cart

admin.site.register(ItemModel)
admin.site.register(Comment)
admin.site.register(Cart)
