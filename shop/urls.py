from django.urls import path, include
from .views import ItemViewerAPIView, AddComment

urlpatterns = [
    path('items/', ItemViewerAPIView.as_view()),
    path('addcomment/', AddComment.as_view()),
]