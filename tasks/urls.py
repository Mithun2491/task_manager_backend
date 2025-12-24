from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, CategoryViewSet, AttachmentDownloadViewSet

task_router = DefaultRouter()
task_router.register(r"tasks", TaskViewSet, basename="task")

category_router = DefaultRouter()
category_router.register(r"", CategoryViewSet, basename="category")

attachment_router = DefaultRouter()
attachment_router.register(r"", AttachmentDownloadViewSet, basename="attachment")

urlpatterns = [
    path("", include(task_router.urls)),                  # /api/tasks/tasks/
    path("categories/", include(category_router.urls)),   # /api/tasks/categories/
    path("attachments/", include(attachment_router.urls)),
]
