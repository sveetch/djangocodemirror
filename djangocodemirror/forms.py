# -*- coding: utf-8 -*-
"""
Forms
"""
from django import forms

from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from djangocodemirror import settings_local
from djangocodemirror.widgets import CodeMirrorWidget
from djangocodemirror.fields import DjangoCodeMirrorField

THEME_CHOICES = [(v.split('/')[-1].split('.')[0], k) for k,v in settings_local.CODEMIRROR_THEMES]

# Try import for parser
try:
    from rstview.parser import SourceReporter, map_parsing_errors
except ImportError:
    # Dummy fallback
    def map_parsing_errors(error, *args, **kwargs):
        # Translators: Dummy error to return when no supported parser is installed
        return ugettext("Dummy")
    def SourceReporter(source, *args, **kwargs):
        return []

# Try import for django-crispy-forms
try:
    from crispy_forms.helper import FormHelper
    from crispy_forms.layout import Submit
except ImportError:
    # Dummy fallback
    def get_form_helper():
        return None
else:
    def get_form_helper():
        helper = FormHelper()
        helper.form_action = '.'
        helper.form_style = 'inline'
        helper.add_input(Submit('submit', _('Save')))
        return helper

class DjangoCodeMirrorSampleForm(forms.Form):
    """
    Sample form
    """
    content = DjangoCodeMirrorField(label=u"DjangoCodeMirror", max_length=50000, required=True, config_name='djangocodemirror_sample_demo')
    
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

class DjangoCodeMirrorSettingsForm(forms.Form):
    """
    Editor settings form
    """
    theme = forms.ChoiceField(label=_('theme'), initial=settings_local.DJANGOCODEMIRROR_DEFAULT_THEME, choices=THEME_CHOICES, required=False, help_text=_("The theme to style the editor with."))
    lineWrapping = forms.BooleanField(label=_('line wrapping'), initial=True, required=False, help_text=_("Whether CodeMirror should scroll or wrap for long lines."))
    no_tab_char = forms.BooleanField(label=_('avoid tabulation'), initial=True, required=False, help_text=_("Disable usage of any tabulation character, instead each tabulation will be replaced by 4 space characters."))
    
    def __init__(self, *args, **kwargs):
        self.helper = get_form_helper()
        if self.helper is not None:
            self.helper.form_action = reverse('djangocodemirror-settings')
        
        super(DjangoCodeMirrorSettingsForm, self).__init__(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        no_tab_char = self.cleaned_data.get('no_tab_char')
        # Set the needed options to avoid tabulation character usage
        if no_tab_char:
            self.cleaned_data.update({
                "indentUnit": 4,
                "tabSize": 4,
                "indentWithTabs": False,
            })
        else:
            self.cleaned_data.update({
                "indentWithTabs": True,
            })
        return self.cleaned_data
