from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from base.admin import BaseAdmin
from .models import TenantProfile

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["email", "name", "is_superuser"]
    search_fields = ["name"]
    ordering = ["email"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "name", "password1", "password2"),
            },
        ),
    )


@admin.register(TenantProfile)
class TenantProfileAdmin(BaseAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "name",
                    "address",
                    "document_proof",
                )
            },
        ),
    )
    list_display = ["user", "name",]
    search_fields = ["name"]
