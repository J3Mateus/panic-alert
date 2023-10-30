import django_filters

from apps.school.models import School


class SchoolFilter(django_filters.FilterSet):
    class Meta:
        model = School
        fields = ("id", "responsible", "created_by","deleted_by","is_deleted")