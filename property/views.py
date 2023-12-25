from django.views.generic import ListView

from .models import Property


class HomePageView(ListView):
    """
    Render page for home page with properties.
    """

    model = Property
    context_object_name = "properties"
    template_name = "index.html"


home_page_view = HomePageView.as_view()
