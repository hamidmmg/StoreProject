from django.urls import path, include
from .views import ItemViewerAPIView

urlpatterns = [
    path('items/', ItemViewerAPIView.as_view())
]