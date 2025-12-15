from django.urls import path
from django.views.generic.base import TemplateView

from .views import BasicSampleFormView, ModesSampleFormView


app_name = "demo"


urlpatterns = [
    # Dummy homepage to list demo views
    path("", TemplateView.as_view(template_name="demo/homepage.html"), name="home"),

    # Sample with codemirror in the raw way
    path("raw/", TemplateView.as_view(template_name="demo/raw.html"), name="raw"),

    # Basic form sample
    path(
        "form/",
        BasicSampleFormView.as_view(),
        name="form"
    ),

    # Mode index list
    path(
        "modes/",
        ModesSampleFormView.as_view(),
        name="mode-index"
    ),

    # Basic form sample with specific mode
    path(
        "modes/<slug:mode>/",
        ModesSampleFormView.as_view(),
        name="basic"
    ),
]
