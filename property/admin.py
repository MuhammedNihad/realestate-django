from django.contrib import admin

from base.admin import BaseAdmin
from .models import Property, Unit


@admin.register(Property)
class PropertyAdmin(BaseAdmin):
    """
    Admin class for Property model
    """

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "features",
                    "address",
                    "location",
                )
            },
        ),
    )
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]


@admin.register(Unit)
class UnitAdmin(BaseAdmin):
    """
    Admin class for Unit model
    """

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "property",
                    "rent_cost",
                    "type",
                )
            },
        ),
    )
    list_display = ["property", "rent_cost", "type", "created_at", "updated_at"]
    search_fields = ["name"]
