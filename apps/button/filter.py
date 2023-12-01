import django_filters

from apps.button.models import Button

class ButtonFilter(django_filters.FilterSet):
    class Meta:
        model = Button
        fields = '__all__'