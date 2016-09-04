# -*- coding: utf-8 -*-
"""
Sample views
"""
import os

from django.conf import settings
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from project.forms import SampleForm


class BasicSampleFormView(FormView):
    template_name = 'form.html'
    form_class = SampleForm

    def get_success_url(self):
        return reverse('home')
