from django.urls import path

from .views import home_page_view, property_detail_view, property_search_results_view


urlpatterns = [
    path("", home_page_view, name="home"),
    path("property/<slug:slug>", property_detail_view, name="property_detail"),
    path("search/", property_search_results_view, name="search_results"),
    ]
