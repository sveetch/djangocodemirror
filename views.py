# -*- coding: utf-8 -*-
"""
Sample views
"""
import json, os

from django import forms
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import BaseFormView
from django.http import HttpResponse
from django.utils.translation import ugettext

import djangocodemirror
from djangocodemirror.fields import CodeMirrorField, DjangoCodeMirrorField

try:
    from sveedocuments.parser import SourceParser
except ImportError:
    # Dummy fallback
    def SourceParser(source, *args, **kwargs):
        # Translators: Dummy content returned when no supported parser is installed
        return ugettext("<p>This a dummy preview because <tt>sveedocuments.parser</tt> is not available.</p>")

try:
    from sveedocuments.parser import SourceReporter, map_parsing_errors
except ImportError:
    # Dummy fallback
    def map_parsing_errors(error, *args, **kwargs):
        # Translators: Dummy error to return when no supported parser is installed
        return ugettext("Dummy")
    def SourceReporter(source, *args, **kwargs):
        return []

class DjangoCodeMirrorSampleForm(forms.Form):
    """
    Sample form
    """
    content = DjangoCodeMirrorField(label=u"DjangoCodeMirror", max_length=5000, required=True, codemirror_attrs=djangocodemirror.CODEMIRROR_SETTINGS['djangocodemirror_sample_demo'])
    
    def clean_content(self):
        """
        Parse content to check eventual markup syntax errors and warnings
        """
        content = self.cleaned_data.get("content")
        if content:
            errors = SourceReporter(content)
            if errors:
                raise forms.ValidationError(map(map_parsing_errors, errors))
        return content
    
    def save(self, *args, **kwargs):
        return

class Sample(TemplateView):
    """
    Sample page view
    """
    template_name = "djangocodemirror/sample.html"
    
    def get(self, request, *args, **kwargs):
        path_root = os.path.abspath(os.path.dirname(djangocodemirror.__file__))
        f = open(os.path.join(path_root, "README.rst"))
        content = f.read()
        f.close()
        
        context = {
            'form' : DjangoCodeMirrorSampleForm(),
            'demo_content': content,
        }
        return self.render_to_response(context)

class SamplePreview(View):
    """
    Sample preview view
    """
    def parse_content(self, request, *args, **kwargs):
        content = request.POST.get('content', None)
        if content:
            return SourceParser(content, silent=False)
        return ''

    def get(self, request, *args, **kwargs):
        return HttpResponse('')
    
    def post(self, request, *args, **kwargs):
        content = self.parse_content(request, *args, **kwargs)
        return HttpResponse( content )

class SampleQuicksave(BaseFormView):
    """
    Sample quicksave view
    """
    form_class = DjangoCodeMirrorSampleForm
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('')
    
    def form_valid(self, form):
        content = json.dumps({'status':'form_valid'})
        form.save()
        return HttpResponse(content, content_type='application/json')

    def form_invalid(self, form):
        content = json.dumps({
            'status':'form_invalid',
            'errors': dict(form.errors.items()),
        })
        return HttpResponse(content, content_type='application/json')
