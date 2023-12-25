from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """
    Render page for choosing the type/category of property to post.
    """

    template_name = "index.html"


home_page_view = HomePageView.as_view()
