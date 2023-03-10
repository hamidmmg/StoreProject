from django.urls import path, include
from .views import ItemViewerAPIView, AddComment, AddToCart, CartView

urlpatterns = [
    path('items/', ItemViewerAPIView.as_view()),
    path('addcomment/', AddComment.as_view()),
    path('addtocart/', AddToCart.as_view()),
    path('cartview/', CartView.as_view()),
]