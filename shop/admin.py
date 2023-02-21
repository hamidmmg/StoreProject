from django.contrib import admin
from .models import ItemModel, Comment, Cart, CartItem

admin.site.register(ItemModel)
admin.site.register(Comment)
admin.site.register(Cart)
admin.site.register(CartItem)
