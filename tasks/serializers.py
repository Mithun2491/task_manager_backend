from rest_framework import serializers
from .models import Category, Task, Attachment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "emoji", "color")


class AttachmentSerializer(serializers.ModelSerializer):
    download_url = serializers.SerializerMethodField()

    class Meta:
        model = Attachment
        fields = (
            "id",
            "original_name",
            "size",
            "content_type",
            "uploaded_at",
            "download_url",
        )

    def get_download_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return request.build_absolute_uri(f"/api/tasks/attachments/{obj.id}/download/")
    


class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True,
        required=False,
        allow_null=True,
    )
    attachments = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "emoji",
            "category",
            "category_id",
            "priority",
            "status",
            "start_date",
            "due_date",
            "completed_at",
            "attachments",
            "created_at",
            "updated_at",
        )

    def create(self, validated_data):
        user = self.context["request"].user
        return Task.objects.create(owner=user, **validated_data)
