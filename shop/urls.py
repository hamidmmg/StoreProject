from django.urls import path, include
from .views import ItemViewerAPIView, AddComment, AddToCart

urlpatterns = [
    path('items/', ItemViewerAPIView.as_view()),
    path('addcomment/', AddComment.as_view()),
    path('addtocart/', AddToCart.as_view()),
]