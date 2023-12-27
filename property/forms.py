from django.forms import Form, CharField, ChoiceField
from .models import Unit

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class PropertySearchForm(Form):
    unit = ChoiceField(
        choices=Unit.BedroomType.choices,
        required=False,
        label="",
    )
    search_query = CharField(label="")

    def __init__(self, *args, **kwargs):
        super(PropertySearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("unit", css_class="form-select-sm choose-unit-search-dropdown"),
            Field("search_query", css_class="form-control px-4 h-100", placeholder="Search properties..."),
            Submit("submit", "Search", css_class="btn btn-primary mb-3"),
        )
