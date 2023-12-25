from django.contrib import admin

from base.admin import BaseAdmin
from .models import Property, RentalInformation, Unit


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


@admin.register(RentalInformation)
class RentalInformationAdmin(BaseAdmin):
    """
    Admin class for Rental information model
    """

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "tenant",
                    "unit",
                    "agreement_end_date",
                    "monthly_rent_date",
                )
            },
        ),
    )
    list_display = ["tenant", "unit", "agreement_end_date", "monthly_rent_date"]
    search_fields = ["tenant", "unit"]
