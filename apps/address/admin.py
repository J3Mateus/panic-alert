from django.contrib import admin
from .models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("zipCode", "district", "uf", "location", "publicArea", "created_at", "updated_at")
    search_fields = ("zipCode", "district", "uf", "location", "publicArea")
    
    fieldsets = (
        (None, {"fields": ("zipCode", "district", "uf")}),
        ("Detalhes", {"fields": ("location", "publicArea")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    readonly_fields = ("created_at", "updated_at")
