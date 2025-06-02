# menu/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MenuItemViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('menu-items', MenuItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
