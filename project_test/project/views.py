# -*- coding: utf-8 -*-
"""
Sample views
"""
import io, os

from django.conf import settings

from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from .forms import SampleForm


class BasicSampleFormView(FormView):
    template_name = 'form.html'
    form_class = SampleForm

    def get_success_url(self):
        return reverse('home')


class ModesSampleFormView(BasicSampleFormView):
    template_name = 'modes.html'

    def get_context_data(self, **kwargs):
        context = super(ModesSampleFormView, self).get_context_data(**kwargs)
        context.update({
            'codemirror_mode': self.codemirror_mode,
        })
        return context

    def get_initial(self):
        """
        Try to find a demo source for given mode if any, if finded use it to
        fill the demo textarea.
        """
        initial = {}

        if self.kwargs.get('mode', None):
            filename = "{}.txt".format(self.kwargs['mode'])
            filepath = os.path.join(settings.PROJECT_PATH, 'demo_datas', filename)
            if os.path.exists(filepath):
                with io.open(filepath, 'r', encoding='utf-8') as fp:
                    initial['foo'] = fp.read()

        return initial

    def get(self, request, *args, **kwargs):
        self.codemirror_mode = kwargs.get('mode', None)
        return super(ModesSampleFormView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.codemirror_mode = kwargs.get('mode', None)
        return super(ModesSampleFormView, self).post(request, *args, **kwargs)
