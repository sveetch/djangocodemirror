# -*- coding: utf-8 -*-
"""
Forms
"""
from django import forms

from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _

from djangocodemirror import settings_local
from djangocodemirror.fields import DjangoCodeMirrorField

THEME_CHOICES = [(v.split('/')[-1].split('.')[0], k) for k,v in settings_local.CODEMIRROR_THEMES]

# Try import for parser
try:
    from sveedocuments.parser import SourceReporter, map_parsing_errors
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
    content = DjangoCodeMirrorField(label=u"DjangoCodeMirror", max_length=5000, required=True, codemirror_attrs=settings_local.CODEMIRROR_SETTINGS['djangocodemirror_sample_demo'])
    
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
    #mode = forms.ChoiceField(label=_('mode'), choices=[(k, k) for k,v in settings_local.CODEMIRROR_MODES], required=False, help_text=_("The mode to use."))
    theme = forms.ChoiceField(label=_('theme'), initial=settings_local.DJANGOCODEMIRROR_DEFAULT_THEME, choices=THEME_CHOICES, required=False, help_text=_("The theme to style the editor with."))
    smartIndent = forms.BooleanField(label=_('smart indent'), initial=True, required=False, help_text=_("Whether to use the context-sensitive indentation that the mode provides (or just indent the same as the line before)."))
    indentUnit = forms.IntegerField(label=_('indent unit'), initial=2, required=True, help_text=_("How many spaces a block (whatever that means in the edited language) should be indented."))
    tabSize = forms.IntegerField(label=_('tab size'), initial=4, required=True, help_text=_("The width of a tab character."))
    indentWithTabs = forms.BooleanField(label=_('indent with tabs'), initial=False, required=False, help_text=_("Whether, when indenting, the first N*tabSize spaces should be replaced by N tabs."))
    lineWrapping = forms.BooleanField(label=_('line wrapping'), initial=False, required=False, help_text=_("Whether CodeMirror should scroll or wrap for long lines."))
    no_tab_char = forms.BooleanField(label=_('avoid tabulation'), initial=False, required=False, help_text=_("Disable usage of any tabulation character, instead each tabulation will be replaced by N space where N is the value of the 'tab size' option."))
    
    def __init__(self, *args, **kwargs):
        self.helper = get_form_helper()
        
        super(DjangoCodeMirrorSettingsForm, self).__init__(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        return self.cleaned_data
