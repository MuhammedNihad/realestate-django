import uuid
from django.db.models import Model, UUIDField, DateTimeField


class BaseModel(Model):
    """
    An abstract base class model that provides UUID as the primary key and
    self-managed created_at and updated_at timestamp fields.
    """

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
