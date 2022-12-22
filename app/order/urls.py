from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', OrderAPIView)


urlpatterns = [
    path('', include(router.urls)),
    path('confirm/<uuid:code>/', OrderConfirmationAPIView.as_view())
]
