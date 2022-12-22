from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.feedback.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.feedback.models import (
    Comment,
)


class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)