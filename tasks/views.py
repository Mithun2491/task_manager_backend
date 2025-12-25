from django.shortcuts import render

# Create your views here.
from django.http import FileResponse, Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Task, Attachment
from .serializers import (
    CategorySerializer,
    TaskSerializer,
    AttachmentSerializer,
)
from .permissions import IsOwner
from .filters import TaskFilter


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    def get_queryset(self):
        # Soft delete handled by is_deleted flag
        return Task.objects.filter(owner=self.request.user, is_deleted=False)
    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    @action(detail=True, methods=["post"], url_path="attachments")
    def upload_attachment(self, request, pk=None):
        """
        Upload a single file to this task.
        """
        task = self.get_object()
        file = request.FILES.get("file")

        if not file:
            return Response(
                {"detail": "No file provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        attachment = Attachment.objects.create(
            task=task,
            file=file,
            original_name=file.name,
            size=file.size,
            content_type=getattr(file, "content_type", ""),
        )
        serializer = AttachmentSerializer(
            attachment, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AttachmentDownloadViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, pk=None):
        try:
            attachment = Attachment.objects.select_related("task").get(
                pk=pk, task__owner=request.user
            )
        except Attachment.DoesNotExist:
            raise Http404

        response = FileResponse(
            attachment.file.open("rb"),
            as_attachment=True,
            filename=attachment.original_name,
        )
        return response
