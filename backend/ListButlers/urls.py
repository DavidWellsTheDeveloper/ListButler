from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'list', ListViewSet)
router.register(r'listitem', ListItemViewSet)
router.register(r'listuser', ListUserViewSet)

urlpatterns = [
    path("", include(router.urls))
]