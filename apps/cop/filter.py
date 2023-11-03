import django_filters

from apps.cop.models import COP


class CopFilter(django_filters.FilterSet):
    class Meta:
        model = COP
        fields = ("id", "responsible", "created_by","deleted_by","is_deleted")