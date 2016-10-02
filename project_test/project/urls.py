"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os

from django.conf import settings
from django.conf.urls import include, url

from django.views.generic.base import TemplateView

from views import BasicSampleFormView, ModesSampleFormView

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),

    # Dummy homepage just for simple ping view
    url(r'^$', TemplateView.as_view(
        template_name="homepage.html"
    ), name='home'),

    # Sample with codemirror in the raw way
    url(r'^raw/$', TemplateView.as_view(
        template_name="raw.html"
    ), name='raw'),

    # Mode index
    url(r'^form/$', BasicSampleFormView.as_view(
        template_name="form.html"
    ), name='form'),

    # Mode index
    url(r'^modes/$', ModesSampleFormView.as_view(
        template_name="modes.html"
    ), name='mode-index'),

    # Basic usage with a mode from a form
    url(r'^modes/(?P<mode>[-\w]+)/$', ModesSampleFormView.as_view(
        template_name="modes.html"
    ), name='basic'),
]
