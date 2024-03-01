from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134168ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134168", Testconnectors134168ViewSet, basename="testconnectors134168"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
