import django_filters

from apps.counties.models import Counties


class CountieFilter(django_filters.FilterSet):
    class Meta:
        model = Counties
        fields = ("id", "code")