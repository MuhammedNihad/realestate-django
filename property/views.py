from django.views.generic import DetailView, ListView

from .models import Property


class HomePageView(ListView):
    """
    Render page for home page with properties.
    """

    model = Property
    context_object_name = "properties"
    template_name = "index.html"


home_page_view = HomePageView.as_view()


class PropertyDetailView(DetailView):
    """
    Render detail view of property
    """

    model = Property
    context_object_name = "property"
    template_name = "property-single.html"

property_detail_view = PropertyDetailView.as_view()
