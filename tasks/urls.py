from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, CategoryViewSet, AttachmentDownloadViewSet

router = DefaultRouter()
router.register(r"", TaskViewSet, basename="task")          # 🔥 FIX HERE
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"attachments", AttachmentDownloadViewSet, basename="attachment-download")

urlpatterns = [
    path("", include(router.urls)),
]
