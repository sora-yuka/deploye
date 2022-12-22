from django.urls import path, include
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from django.conf import settings
from django.conf.urls.static import static
schema_view = get_schema_view(
    openapi.Info(
        title='Python 24 shop',
        default_version='v1',
        description='Интернет магазин'
    ),
    public=True
)

from app.product.views import (
    ProductAPIView, CategoryAPIView
)

router = DefaultRouter()
router.register('category', CategoryAPIView)
router.register('', ProductAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
