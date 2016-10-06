========
Examples
========

This will assume you have followed :ref:`install-intro` document.

For a HTML element
------------------

For this example we will attach a CodeMirror instance with ``restructuredtext``
mode directly to a HTML element through its HTML identifier (``id``).

#. Create a ``editor.html`` file:

    .. sourcecode:: html

        {% load djangocodemirror_tags %}

        <form>
            <textarea id="code" name="code">Lorem ipsum dolor sit amet.</textarea>
        </form>

        {% codemirror_instance 'restructuredtext' 'code_codemirror' 'code' %}

#. Register your view in ``urls.py`` file:

    .. sourcecode:: python

        from django.conf.urls import include, url

        from django.views.generic.base import TemplateView

        urlpatterns = [

            url(r'^editor/$', TemplateView.as_view(
                template_name="editor.html"
            ), name='editor'),

        ]

For a form field
----------------

For this example we will attach a CodeMirror instance with
``restructuredtext`` to a form field.

#. Create a ``forms.py`` file:

    .. sourcecode:: python

        from django import forms

        from djangocodemirror.fields import CodeMirrorField

        class SampleForm(forms.Form):
            foo = CodeMirrorField(label="Foo", required=True,
                                  config_name="restructuredtext")

#. Create a ``view.py`` file:

    .. sourcecode:: python

        from django.views.generic.edit import FormView
        from django.core.urlresolvers import reverse

        from .forms import SampleForm


        class BasicSampleFormView(FormView):
            template_name = 'form.html'
            form_class = SampleForm

            def get_success_url(self):
                return reverse('codemirror-form')

#. Create a ``form.html`` file:

    .. sourcecode:: html

        {% load djangocodemirror_tags %}

        <form action="." method="post">{% csrf_token %}
            {{ form.as_p }}
            <input type="submit">
        </form>

        {% codemirror_field_css_assets form.foo %}
        {% codemirror_field_js_assets form.foo %}
        <script>
            var foo_codemirror = CodeMirror.fromTextArea(
                document.getElementById("id_foo"),
                {{ form.foo|codemirror_parameters }}
            );
        </script>

#. Register your view in ``urls.py`` file:

    .. sourcecode:: python

        from django.conf.urls import include, url

        from views import BasicSampleFormView

        urlpatterns = [

            url(r'^form/$', BasicSampleFormView.as_view(
                template_name="form.html"
            ), name='codemirror-form'),

        ]
