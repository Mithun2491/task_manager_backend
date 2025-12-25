from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, CategoryViewSet, AttachmentDownloadViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"attachments", AttachmentDownloadViewSet, basename="attachments")

urlpatterns = [
    path("", include(router.urls)),
]
