from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, CategoryViewSet, AttachmentDownloadViewSet

router = DefaultRouter()
router.register(r"", TaskViewSet, basename="task")
router.register(r"categories", CategoryViewSet, basename="task-categories")
router.register(r"attachments", AttachmentDownloadViewSet, basename="attachment")

urlpatterns = [
    path("", include(router.urls)),
]
