import uuid
from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    CharField,
    EmailField,
    FileField,
    OneToOneField,
    TextField,
    UUIDField,
)
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField

from base.models import BaseModel
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Default custom user model.
    """

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None
    last_name = None
    username = None
    email = EmailField(_("Email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        """
        Return a string representation of the object.
        """
        return self.email


class TenantProfile(BaseModel):
    """
    Represents a tenant user's profile.

    Attributes:
        user (OneToOneField): The user model associated with this tenant profile.
        name (CharField): The name of the tenant user.
        address (TextField): The address of the tenant user.
        document_proof (FileField): The document proof file of the tenant user.
    """

    user = OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = CharField(
        _("Name of tenant user"),
        max_length=255,
        help_text=_("Specify the name of the tenant user."),
    )
    address = TextField(
        _("Address of tenant user"),
        help_text=_("Specify the address of the tenant user."),
    )
    document_proof = FileField(
        _("Document proof of tenant user"),
        upload_to=("uploads/document-proofs/%Y/%m/%d/"),
        help_text=_("Upload/update a document proof file of tenant user"),
    )
    slug = AutoSlugField(
        populate_from="name",
        help_text=_("Automatically generated slug based on the name."),
    )


    class Meta:
        verbose_name = "Tenant Profile"
        verbose_name_plural = "Tenant Profiles"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Profile of {self.name}"

    def get_absolute_url(self):
        """
        Get url for tenant user's detail view.

        Returns:
            str: URL for user detail.
        """
        return reverse("tenant_detail", kwargs={"slug": self.slug})
