from django.urls import path

from .views import tenant_profile_detail_view


urlpatterns = [
    path("tenant/<slug:slug>", tenant_profile_detail_view, name="tenant_detail"),
]
