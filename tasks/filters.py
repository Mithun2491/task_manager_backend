import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    min_due_date = django_filters.DateTimeFilter(
        field_name="due_date", lookup_expr="gte"
    )
    max_due_date = django_filters.DateTimeFilter(
        field_name="due_date", lookup_expr="lte"
    )

    class Meta:
        model = Task
        fields = ["status", "priority", "category", "min_due_date", "max_due_date"]
