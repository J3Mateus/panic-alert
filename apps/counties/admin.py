from django.contrib import admin, messages
from django.forms import ValidationError
from apps.counties.models import Counties

@admin.register(Counties)
class CountiesAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "released", "created_at", "updated_at")

    search_fields = ("name", "code")

    list_filter = ("released",)

    fieldsets = (
        (None, {"fields": ("name", "code", "released")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    def save_model(self, request, obj, form, change):
        if change:
            return super().save_model(request, obj, form, change)

        try:
            # Adicione aqui a lógica necessária para criar o objeto Counties
            obj.save()
        except ValidationError as exc:
            self.message_user(request, str(exc), messages.ERROR)
