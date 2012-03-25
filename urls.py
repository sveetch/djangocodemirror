# -*- coding: utf-8 -*-
"""
Url map for sample views
"""
from django.conf.urls.defaults import *

from djangocodemirror.views import Sample, SamplePreview, SampleQuicksave

urlpatterns = patterns('',
    url(r'^$', Sample.as_view(), name='djangocodemirror-sample-view'),
    url(r'^preview/$', SamplePreview.as_view(), name='djangocodemirror-sample-preview'),
    url(r'^quicksave/$', SampleQuicksave.as_view(), name='djangocodemirror-sample-quicksave'),
)
