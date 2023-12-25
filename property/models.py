from django.db.models import CharField, TextField, URLField
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class Property(BaseModel):
    """
    Represents a property with a name, address, and optional Google Maps link.

    Attributes:
        name (CharField): The name of the property.
        features (TextField): The features or amenities of property
        address (TextField): The address of the property.
        location (URLField): The Google Maps link of the property (optional).

    Returns:
        str: property instance with name as the string representation
    """

    name = CharField(
        _("Name of property"),
        max_length=255,
        help_text=_("Specify the name of the category."),
    )
    features = TextField(
        _("Features of Property"),
        blank=True,
        default="",
        help_text=("Specify features or amenities of property."),
    )
    address = TextField(
        _("Address of property"),
        help_text=_("Specify the address of the property."),
    )
    location = URLField(
        _("Google map of property"),
        blank=True,
        default="",
        help_text=_("Google Maps Link (Optional)."),
    )

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        ordering = ["-created_at"]

    def __str__(self):
        """
        Returns name of property as the string representation of the object.
        """
        return self.name
