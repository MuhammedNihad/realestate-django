from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    """
    A base admin class that provides common configurations for model admins.

    Attributes:
        list_filter (list): A list of fields that can be used to filter the model list view.
        readonly_fields (list): A list of fields that are displayed as read-only in the admin interface.
    """

    list_filter = ["created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
