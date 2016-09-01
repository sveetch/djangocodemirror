# -*- coding: utf-8 -*-
"""
Sample views
"""
import os

from django.views.generic.base import TemplateView
from django.conf import settings

#from djangocodemirror.forms import DjangoCodeMirrorSampleForm

class BasicSampleView(TemplateView):
    """
    Sample basic view
    """
    template_name = "basic.html"

    #def get(self, request, *args, **kwargs):
        #path_root = os.path.abspath(os.path.dirname(rstview_local_settings.__file__))
        #f = open(os.path.join(path_root, "rst_sample.rst"))
        #content = f.read()
        #f.close()

        #context = {
            #'form' : DjangoCodeMirrorSampleForm(),
            #'demo_content': content,
        #}
        #return self.render_to_response(context)
