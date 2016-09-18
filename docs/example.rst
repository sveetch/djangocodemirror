=======
Example
=======

For this example we will build a restructuredtext editor in a form with CodeMirror *search* addon and with *Ambiance* theme.

#. Add editor settings in **settings.py**:

    .. sourcecode:: python

        from djangocodemirror.settings import *

        CODEMIRROR_SETTINGS = {
            'empty': {},
            'rst-editor': {
                'mode': 'rst',
                'lineWrapping': True,
                'lineNumbers': True,
                'addons': [
                    "CodeMirror/lib/util/dialog.js",
                    "CodeMirror/lib/util/search.js",
                    "CodeMirror/lib/util/searchcursor.js",
                ],
            },
        }

        CODEMIRROR_THEMES = {
            "ambiance": "CodeMirror/theme/ambiance.css",
        }

        CODEMIRROR_MODES = {
            "rst": "CodeMirror/mode/rst/rst.js",
        }

#. Create a **forms.py** file:

    .. sourcecode:: python

        from django import forms

        from djangocodemirror.fields import CodeMirrorField

        class SampleForm(forms.Form):
            foo = CodeMirrorField(label="Foo",
                                required=True,
                                config_name="rst-editor",
                                initial='Hello World!')

#. Then create a **view.py** file:

    .. sourcecode:: python

        from django.views.generic.edit import FormView
        from django.core.urlresolvers import reverse

        from .forms import SampleForm


        class BasicSampleFormView(FormView):
            template_name = 'form.html'
            form_class = SampleForm

            def get_success_url(self):
                return reverse('home')

    Note the ``reverse`` part, you may have an url name ``home`` in your urls or change it to another one.
