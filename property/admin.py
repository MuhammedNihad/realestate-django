from django.contrib import admin

from base.admin import BaseAdmin
from .models import Property


@admin.register(Property)
class PropertyAdmin(BaseAdmin):
    """
    Admin class for Property model
    """

    fieldsets = (
        (
            None,
            {"fields": ("name", "features", "address", "location",)},
        ),
    )
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
