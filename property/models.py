from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    DecimalField,
    ForeignKey,
    TextChoices,
    TextField,
    URLField,
)
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse

from base.models import BaseModel
from accounts.models import TenantProfile


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
    slug = AutoSlugField(
        populate_from="name",
        help_text=_("Automatically generated slug based on the name."),
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

    def get_absolute_url(self):
        """
        Return the absolute url of property.
        """
        return reverse("property_detail", args=[str(self.slug)])


class Unit(BaseModel):
    """
    A model representing a unit in a property.
    """

    class BedroomType(TextChoices):
        """Choices for the bedroom type of the unit."""

        ONE_BHK = "1BHK", _("1BHK")
        TWO_BHK = "2BHK", _("2BHK")
        THREE_BHK = "3BHK", _("3BHK")
        FOUR_BHK = "4BHK", _("4BHK")

    property = ForeignKey(Property, on_delete=CASCADE, related_name="units")
    rent_cost = DecimalField(
        _("Rent cost of unit"),
        max_digits=10,
        decimal_places=2,
        help_text=_("Specify the current price of the product."),
    )
    type = CharField(
        _("Bedroom type of unit"),
        max_length=10,
        choices=BedroomType.choices,
        default=BedroomType.ONE_BHK,
        help_text=_("Choose Bedroom type of unit"),
    )
    slug = AutoSlugField(
        populate_from=["property", "type"],
        help_text=_(
            "Automatically generated slug based on the property name and type."
        ),
    )

    class Meta:
        verbose_name = "Unit"
        verbose_name_plural = "Units"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.type} unit of {self.property.name}"


class RentalInformation(BaseModel):
    """
    Represents rental information for a property unit.

    Attributes:
        tenant (ForeignKey): Foreign key to the TenantProfile model representing the tenant associated with this rental information.
        unit (ForeignKey): Foreign key to the Unit model representing the rental unit associated with this rental information.
        agreement_end_date (DateField): Date field representing the end date of the rental agreement.
        monthly_rent_date (DateField): Date field representing the date on which the monthly rent is due.
    """

    tenant = ForeignKey(TenantProfile, on_delete=CASCADE)
    unit = ForeignKey(Unit, on_delete=CASCADE)
    agreement_end_date = DateField()
    monthly_rent_date = DateField()
    slug = AutoSlugField(
        populate_from=[
            "tenant",
            "unit",
        ],
        help_text=_("Automatically generated slug based on the tenant name and unit."),
    )

    class Meta:
        verbose_name = "Rental Information"
        verbose_name_plural = "Rental Information"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Rental info of {self.unit}"
