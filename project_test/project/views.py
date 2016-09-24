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

    def get_context_data(self, **kwargs):
        context = super(BasicSampleFormView, self).get_context_data(**kwargs)
        context.update({
            'codemirror_mode': self.codemirror_mode,
        })
        return context

    def get(self, request, *args, **kwargs):
        self.codemirror_mode = kwargs.get('mode', None)
        return super(BasicSampleFormView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.codemirror_mode = kwargs.get('mode', None)
        return super(BasicSampleFormView, self).post(request, *args, **kwargs)
