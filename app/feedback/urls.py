from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.feedback.views import (
    CommentAPIView
)

router = DefaultRouter()
router.register('', ommentAPIView)

urlpatterns = [
    path('', include(router.urls))
]
