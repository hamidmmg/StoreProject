from django.shortcuts import render
from rest_framework import generics
from .models import ItemModel
from .serializers import ItemSerializer


class ItemViewerAPIView(generics.ListAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer