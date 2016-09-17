# -*- coding: utf-8 -*-
"""
Sample views
"""
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from .forms import SampleForm


class BasicSampleFormView(FormView):
    template_name = 'form.html'
    form_class = SampleForm

    def get_success_url(self):
        return reverse('home')
