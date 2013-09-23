# -*- coding: utf-8 -*-
"""
Sample views
"""
import datetime, json, os, urllib
import base64

from django.views.generic.base import View, TemplateView
from django.views.generic.edit import BaseFormView, FormView
from django.http import HttpResponse
from django.utils.translation import ugettext
from django.conf import settings

from rstview import local_settings as rstview_local_settings

from djangocodemirror import settings_local
from djangocodemirror.forms import DjangoCodeMirrorSampleForm, DjangoCodeMirrorSettingsForm

try:
    from rstview.parser import SourceParser
except ImportError:
    # Dummy fallback
    def SourceParser(source, *args, **kwargs):
        # Translators: Dummy content returned when no supported parser is installed
        return ugettext("<p>This a dummy preview because <tt>sveedocuments.parser</tt> is not available.</p>")

class SampleView(TemplateView):
    """
    Sample page view
    """
    template_name = "djangocodemirror/sample.html"
    
    def get(self, request, *args, **kwargs):
        path_root = os.path.abspath(os.path.dirname(rstview_local_settings.__file__))
        f = open(os.path.join(path_root, "rst_sample.rst"))
        content = f.read()
        f.close()
        
        context = {
            'form' : DjangoCodeMirrorSampleForm(),
            'demo_content': content,
        }
        return self.render_to_response(context)

class SamplePreviewMixin(object):
    """
    Sample preview mixin
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

class SamplePreviewView(SamplePreviewMixin, View):
    """
    Sample preview view
    """
    pass

class SampleQuicksaveMixin(object):
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

class SampleQuicksaveView(SampleQuicksaveMixin, BaseFormView):
    """
    Sample quicksave view
    """
    pass

class EditorSettingsMixin(object):
    """
    Editor Settings mixin
    """
    form_class = DjangoCodeMirrorSettingsForm

    def get_template_names(self):
        if self.request.is_ajax():
            return ["djangocodemirror/include_settings_form.html"]
        return ["djangocodemirror/settings.html"]

    def get_initial(self):
        """
        Try to get the initial data from saved cookie
        """
        user_settings = self.request.COOKIES.get(settings_local.DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME, None)
        if user_settings:
            return json.loads(urllib.unquote(user_settings))
        return {}
    
    def patch_response(self, response, saved_settings):
        """
        Patch response to save user settings in a cookie
        """
        cookie_content = json.dumps(saved_settings)
        cookie_expires = datetime.datetime.strftime(
            datetime.datetime.utcnow() + datetime.timedelta(seconds=settings_local.DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_MAXAGE), 
            "%a, %d-%b-%Y %H:%M:%S GMT"
        )
        
        response.set_cookie(
            settings_local.DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME,
            urllib.quote(cookie_content),
            max_age=settings_local.DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_MAXAGE,
            expires=cookie_expires,
            domain=settings.SESSION_COOKIE_DOMAIN
        )
        
        return response
    
    def form_valid(self, form):
        """
        Save settings in cookies and back to the form with a success message
        """
        saved_settings = form.save()
        
        if self.request.is_ajax():
            content = json.dumps({'status':'form_valid', 'setting_options':saved_settings})
            resp = HttpResponse(content, content_type='application/json')
        else:
            form_class = self.get_form_class()
            new_form = self.get_form(form_class)
            resp = self.render_to_response(self.get_context_data(form=new_form, save_success=True))
        
        return self.patch_response(resp, saved_settings)

    def form_invalid(self, form):
        if self.request.is_ajax():
            content = json.dumps({
                'status':'form_invalid',
                'errors': dict(form.errors.items()),
            })
            return HttpResponse(content, content_type='application/json')
        
        return super(EditorSettings, self).form_invalid(form)

class EditorSettingsView(EditorSettingsMixin, FormView):
    """
    Editor Settings view
    """
    pass
