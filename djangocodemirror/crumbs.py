# -*- coding: utf-8 -*-
"""
Application Crumbs
"""
from autobreadcrumbs import site
from django.utils.translation import ugettext_lazy

site.update({
    'djangocodemirror-sample-view': ugettext_lazy('DjangoCodeMirror sample'),
    'djangocodemirror-settings': ugettext_lazy('Your settings'),
})
