"""
Sandbox URL Configuration
"""
from django.conf import settings
from django.conf.urls import url

from django.views.generic.base import TemplateView

from sandbox.views import BasicSampleFormView, ModesSampleFormView


urlpatterns = [
    # Dummy homepage to list demo views
    url(r'^$', TemplateView.as_view(
        template_name="homepage.html"
    ), name='home'),

    # Sample with codemirror in the raw way
    url(r'^raw/$', TemplateView.as_view(
        template_name="raw.html"
    ), name='raw'),

    # Basic form sample
    url(r'^form/$', BasicSampleFormView.as_view(
        template_name="form.html"
    ), name='form'),

    # Mode index list
    url(r'^modes/$', ModesSampleFormView.as_view(
        template_name="modes.html"
    ), name='mode-index'),

    # Basic form sample with specific mode
    url(r'^modes/(?P<mode>[-\w]+)/$', ModesSampleFormView.as_view(
        template_name="modes.html"
    ), name='basic'),
]
