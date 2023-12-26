from django.views.generic import DetailView, FormView, ListView
from django.db.models import Q

from .forms import PropertySearchForm
from .models import Property


class HomePageView(ListView, FormView):
    """
    Render page for home page with properties.
    """

    model = Property
    context_object_name = "properties"
    template_name = "index.html"
    form_class = PropertySearchForm


home_page_view = HomePageView.as_view()

class PropertySearchResultsView(ListView, FormView):
    """
    Render search results.
    """

    context_object_name = "search_result"
    template_name = "search-results.html"
    form_class = PropertySearchForm

    def get_queryset(self):
        """
        Perform search and return results.
        """

        unit = self.request.GET.get("unit", None)
        search_query = self.request.GET.get("search_query", None)

        if unit and search_query:
            search_results = Property.objects.filter(
                Q(units__type__icontains=unit) & Q(name__icontains=search_query) | Q(features__icontains=search_query)
            ).distinct()
            return search_results


property_search_results_view = PropertySearchResultsView.as_view()


class PropertyDetailView(DetailView):
    """
    Render detail view of property
    """

    model = Property
    context_object_name = "property"
    template_name = "property-single.html"


property_detail_view = PropertyDetailView.as_view()
