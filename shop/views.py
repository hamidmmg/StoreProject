from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from .models import ItemModel, Comment
from .serializers import ItemSerializer, AddCommentSerializer
from rest_framework.response import Response


class ItemViewerAPIView(generics.ListAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer


class AddComment(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddCommentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        print(request.user)
        serializer.context['user'] = request.user
        serializer.is_valid(raise_exception=True)
        return Response("items deleted successfully", status=status.HTTP_200_OK)
