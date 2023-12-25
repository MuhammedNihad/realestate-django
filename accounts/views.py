from django.views.generic import DetailView

from .models import TenantProfile


class TenantProfileDetailView(DetailView):
    """
    Render detail page of tenant user
    """

    model = TenantProfile
    context_object_name = "tenant"
    template_name = "tenant-detail.html"


tenant_profile_detail_view = TenantProfileDetailView.as_view()
