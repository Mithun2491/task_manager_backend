
# Register your models here.
from django.contrib import admin
from .models import Category, Task, Attachment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "emoji", "color")


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 0


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "status", "priority", "due_date", "is_deleted")
    list_filter = ("status", "priority", "category")
    search_fields = ("title", "description")
    inlines = [AttachmentInline]


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("original_name", "task", "size", "uploaded_at")
