# -*- coding: utf-8 -*-
"""
Url map for sample views
"""
from django.conf.urls.defaults import *

from djangocodemirror.views import SampleView, SamplePreviewView, SampleQuicksaveView, EditorSettingsView

urlpatterns = patterns('',
    url(r'^$', SampleView.as_view(), name='djangocodemirror-sample-view'),
    url(r'^preview/$', SamplePreviewView.as_view(), name='djangocodemirror-sample-preview'),
    url(r'^quicksave/$', SampleQuicksaveView.as_view(), name='djangocodemirror-sample-quicksave'),
    url(r'^settings/$', EditorSettingsView.as_view(), name='djangocodemirror-settings'),
)
