.. _CodeMirror: http://codemirror.net/
.. _CodeMirror Documentation: http://codemirror.net/doc/manual.html
.. _jQuery: http://jquery.com/
.. _jQuery.ajax(): http://api.jquery.com/jQuery.ajax/
.. _Django CSRF: https://docs.djangoproject.com/en/dev/ref/contrib/csrf/
.. _Django staticfiles: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/
.. _Django internationalization system: https://docs.djangoproject.com/en/dev/topics/i18n/
.. _django-assets: http://pypi.python.org/pypi/django-assets
.. _ReStructuredText: http://docutils.sourceforge.net/rst.html

Introduction
============

**Django-CodeMirror** is a Django application to embed the `CodeMirror`_ editor.

It was designed to be used in **sveedocuments**, so it is suited for a
`ReStructuredText`_ environment but `CodeMirror`_ support a large range of syntax
coloration modes (PHP, Python, Ruby, Java, HTML, etc..). It is essentialy a jQuery
plugin on top of `CodeMirror`_ to add some features like :

* A button bar with keyboard shortcuts to use some syntax element in your text;
* A maximize mode to resize the editor at full browser size;
* A preview mode;
* A quicksave option;
* Support translations with english and french allready shipped;
* Compatibility with `Django CSRF`_.

**NOTE :** Since the version 3.0, CodeMirror does not really support IE7 and so Django-CodeMirror too.

Links
*****

* Download his
  `PyPi package <http://pypi.python.org/pypi/djangocodemirror>`_;
* Clone it on his
  `Github repository <https://github.com/sveetch/djangocodemirror>`_;

Requires
========

Your project will have to includes a copy of these Javascript libraries :

* `jQuery`_ >= 1.7 (2.0 has not been tested);
* `CodeMirror`_ == 3.0 but it is allready included as a git submodule or in the Python package;

Optionnally, to use Assets bundles instead of plain assets, you can install `django-assets`_.

Install
=======

The easiest method to install it, is with ``pip`` like this : ::

    pip install djangocodemirror

Or installing it like you want from the Github repository.

Settings
********

In your *settings* file add the app to your installed apps :

::

    INSTALLED_APPS = (
        ...
        'djangocodemirror',
        ...
    )

And you will need to have a copy of `CodeMirror`_ in your *statics* directory (see
`Django staticfiles`_). The jQuery library must be called by your templates,
**Django-CodeMirror** don't do it for you.

Getting CodeMirror
******************

`CodeMirror`_ is included as a git submodule, so you can install it from Github. Within the root of the **Django-CodeMirror** repository do this : ::

    git submodule update --init

This is optionnal, if you want you can download it and install it yourself.

If you have used ``pip`` to install **Django-CodeMirror**, you don't have to mind about this as `CodeMirror`_ is allready shipped in the PyPi package.

Usage
=====

DjangoCodeMirror
****************

`DjangoCodeMirror`_ is the `jQuery`_ plugin on top of `CodeMirror`_, it accepts all
`CodeMirror`_ options and some additional :

fullscreen
    This enable the maximize mode at ``true``. It is enabled by default.
help_link
    Help page link to put in button bar if filled. If the string is empty there will be
    no help button displayed. When clicked the link is opened in a new window.
quicksave_url
    When the string is not empty, it is used as the URL to send data in **POST** request
    where the view receiver should save the data. This is disabled by default. If the
    ``csrf`` option is enabled, it will be used in the request.

    The default sended datas are :

    * ``nocache`` : a timestamp used to block some browser caching, this can be ignored;
    * ``content`` : the textarea content.

    More datas can be sended with the ``quicksave_datas`` option.
quicksave_datas
    Expect an object ``{...}`` whose variables will be sended as data in *quicksave*
    request.

    Or it can be a *string* that determine a variable name to find the object in the
    global context. This is useful if you want to use a variable that can change and not
    a defined object at page load.
preview_url
    When the string is not empty, it is used as the URL to send data in **POST** request
    where the view receiver should render the content with a parser. The excepted
    response must return the HTML fragment rendered. This is disabled by default. If the
    ``csrf`` option is enabled, it will be used in the request.

    The default sended datas are :

    * ``nocache`` : a timestamp used to block some browser caching, this can be ignored;
    * ``content`` : the textarea content.
csrf
    Expect a *string* containing the function name which be used to modify a request to
    add it the needed *token* by `Django CSRF`_. The token will be injected in the
    request headers. A ready to use function is allready shipped.

    The function have two required arguments :

    * xhr : the `jQuery`_ XMLHTTPRequest to be modified;
    * settings : the settings object used with `jQuery.ajax()`_.

    You should see the option ``beforeSend`` of `jQuery.ajax()`_ for more details, this
    is where the csrf function is really used.
display_cursor_position
    At ``True`` it enable the display of current line and column in the bottom right of
    the editor. This option is enabled by default.
no_tab_char
    At ``True`` the usage of the tabulation key will not write a tabulation character and
    spaces will be writed in replacment. The number of spaces will be determined from the
    *tabSize* option (default to 4) from CodeMirror.
undo_buttons
    At ``True`` it display buttons *Undo* and *Redo* in the buttons bar. Enabled by
    default.
settings_cookie
    When the string is not empty, it is used as the cookie name where to search settings
    to overwrite the default ones (of Django-CodeMirror).
search_enabled
    Only for your application settings, the plugin doesn't know of this option. At
    ``True`` this will enable the *search & replace* feature of `CodeMirror`_. This is
    enabled by default for `DjangoCodeMirrorField`_ and the demo settings.

A full example of these settings with the plugin :

::

    <div>
        <textarea id="id_content" rows="10" cols="40" name="content"></textarea>
        <script language="JavaScript" type="text/javascript">
        //<![CDATA[
            my_datas = {'foo': 'bar'};
            $(document).ready(function() {
                id_content_codemirror_instance = $('#id_content').djangocodemirror({
                    "mode": "rst",
                    "csrf": "CSRFpass",
                    "fullscreen": true,
                    "help_link": "/help/",
                    "quicksave_url": "/djangocodemirror-sample/quicksave/",
                    "quicksave_datas": my_datas,
                    "preview_url": "/djangocodemirror-sample/preview/",
                    "display_cursor_position": true,
                    "no_tab_char": true,
                    "undo_buttons": true,
                    "settings_cookie": "djancocodemirror_settings",
                    "lineNumbers": true
                });
            });
        //]]>
        </script>
    </div>

The plugin use some additional libraries (allready shipped) :

* `jquery.cookie <https://github.com/carhartl/jquery-cookie>`_ >= 1.3.1 but note that if you use Foundation5 this library is allready shipped in its vendor Javascript libraries;

.. NOTE:: If you directly use the plugin, you will have to load yourself all needed
          libaries, see `Fields static files`_ for a details of these.

.. WARNING:: Previous versions (<0.7.2) was automatically loading the Javascript init
             for the field. This is not the default behavior anymore. You should see the
             ``embed_settings`` widget attribute to enable this behavior. Else you will
             use the default behavior and manually load the needed Javascript using the
             given `Template tags`_.

CodeMirrorWidget
****************

This is the widget to use in your form fields to apply them an instance of
`DjangoCodeMirror`_ or `CodeMirror`_. It is accessible at
``djangocodemirror.fields.CodeMirrorWidget``.

Usage example on a form field :

::

    from djangocodemirror.fields import CodeMirrorWidget

    class CodeMirrorSampleForm(forms.Form):
        content = forms.CharField(label=u"Your content", widget=CodeMirrorWidget)

        def save(self, *args, **kwargs):
            return

The widget accept some additional arguments :

* ``codemirror_only`` A *boolean* to disable the `DjangoCodeMirror`_ usage at benefit of
  `CodeMirror`_. It is ``False`` by default;
* ``config_name`` : name of the settings to use, a valid key name from
  ``settings.CODEMIRROR_SETTINGS``;
* ``codemirror_settings_extra`` an optional dict to override some settings;
* ``embed_settings`` : A *boolean* to active the automatic embed of the needed
  Javascript code to launch a CodeMirror instance for the field. This is ``False``
  by default because there is lots of possible scenarios to manage your assets and
  Javascript code. So if you active this, DjangoCodeMirror assets must be loaded
  BEFORE your field appear in the HTML code;

Another example where the ``content`` field will be a `CodeMirror`_ editor with enabled
line numbers :

::

    from djangocodemirror.fields import CodeMirrorWidget

    class CodeMirrorSampleForm(forms.Form):
        content = forms.CharField(label="Your content", widget=CodeMirrorWidget(config_name='default'}))

        def save(self, *args, **kwargs):
            return

Note that previously, ``CodeMirrorWidget`` required the ``codemirror_attrs`` to directly receives settings as a dict. This is not the behavior anymore, because the widget was not aware of the settings name that is needed with the Assets bundle system. If you don't want to use Assets bundles and want to directly specify settings as a dict, you will have to use the ``CodeMirrorAttrsWidget`` that accepts the same argument as ``CodeMirrorWidget`` but with ``codemirror_attrs`` instead of ``config_name``.

Using within the Django admin
-----------------------------

To use the plugin within your model forms without to edit their admin templates or admin forms, you will have to specify some special arguments. The process is to use the ``_media`` property so the admin can automatically load all of them.

So for example with a model like this : ::

    class MyModel(models.Model):
        title = models.CharField('title', blank=False, max_length=255)
        content = models.TextField('content', blank=False)

You would have a model admin like this : ::

    class MyModelAdmin(admin.ModelAdmin):
        formfield_overrides = {
            models.TextField: {'widget': CodeMirrorWidget(config_name='default', embed_settings=True)},
        }

Note the ``embed_settings``, it specifies to add the Javascript settings directly bellow the textarea tag and the second one;

CodeMirrorField
***************

This inherit from ``django.forms.CharField`` to automatically use `CodeMirrorWidget`_ as
the widget field. The widget set the ``codemirror_only`` attribute to ``True`` to use
only the `CodeMirror`_ editor.

It take an additional named argument ``config_name`` like `CodeMirrorWidget`_, his
default value correspond to the ``default`` setting of `CODEMIRROR_SETTINGS`_.

::

    from django import forms
    from djangocodemirror.fields import CodeMirrorField

    class CodeMirrorSampleForm(forms.Form):
        content_codemirror = CodeMirrorField(label=u"Your content", config_name='default'})

        def save(self, *args, **kwargs):
            return

DjangoCodeMirrorField
*********************

It is identical as `CodeMirrorField`_ but for usage of `DjangoCodeMirror`_ as the widget
field.

His default value for ``config_name`` corresponds to
`DJANGOCODEMIRROR_DEFAULT_SETTING`_.

::

    from django import forms
    from djangocodemirror.fields import CodeMirrorField

    class CodeMirrorSampleForm(forms.Form):
        content_djangocodemirror = DjangoCodeMirrorField(label=u"Your content", config_name='djangocodemirror'})

        def save(self, *args, **kwargs):
            return

Application settings
====================

All default app settings is located in the ``settings_local.py`` file of
``djangocodemirror``, you can modify them in your project settings using
the ``CODEMIRROR_SETTINGS`` setting.

CODEMIRROR_FIELD_INIT_JS
************************

**Type :** *string*

HTML code to instantiate `CodeMirror`_ in form fields, this is a template string (usable
with ``String.format()``) which expect two variable places :

* ``{inputid}`` : Will be the unique field id;
* ``{settings}`` : Will be a JSON string representation of the editor settings.

DJANGOCODEMIRROR_FIELD_INIT_JS
******************************

**Type :** *string*

This identical to `CODEMIRROR_FIELD_INIT_JS`_ but for `DjangoCodeMirror`_ usage only.

CODEMIRROR_SETTINGS
*******************

**Type :** *dict*

The settings schemes to use with `CodeMirror`_ and `DjangoCodeMirror`_ editors. Each
editor form fields use this schemes to get their default settings. Note that these
options must be suitable to be transformed by the Python JSON parser.

The default available settings schemes are :

* ``default`` : Only for enable the option to show line numbers;
* ``djangocodemirror`` : Minimal options for `DjangoCodeMirror`_ (line numbers and mode
  ``rst`` for `ReStructuredText`_);
* ``djangocodemirror_with_preview`` : Same as ``djangocodemirror`` but enable the
  preview option on ``preview/``;
* ``djangocodemirror_sample_demo`` : Same as ``djangocodemirror`` but enable all stuff
  needed in the `Sample demonstration`_.

DJANGOCODEMIRROR_DEFAULT_SETTING
********************************

**Type :** *string*

The keyword to use to select the default settings with `DjangoCodeMirrorField`_. Note
that `CodeMirrorField`_ always use the keyword ``default`` to select his default
settings.

DJANGOCODEMIRROR_TRANSLATIONS
*****************************

**Type :** *list* or *tuple*

A list of paths for available translations.

CODEMIRROR_THEMES
*****************

**Type :** *list* or *tuple*

A list of paths for available themes to load with `CodeMirror`_. There is actually no
loaded theme by default, you will have to set one in your `CODEMIRROR_SETTINGS`_

CODEMIRROR_MODES
****************

**Type :** *list* or *tuple*

A list of tuples for the various syntax coloration modes supported by `CodeMirror`_.
This list is generated from the available mode files in `CodeMirror`_.

Fields static files
===================

All given paths will be assumed to be in your staticfiles directory
(see `Django staticfiles`_).

Direct assets
*************

If you plan to use the simple assets system, they are now defined in the
``templates/djangocodemirror/include_field_assets.html`` template, with some conditional
includes from the widget settings. This is the default template used with the
``djangocodemirror_get_assets`` template filter.

Bundle assets
*************

If you plan to only use Bundle assets with `django-assets`_, assets are defined in the
``assets.py`` module that is automatically loaded by `django-assets`_. You will have to
use the ``djangocodemirror_get_bundles`` template filter, that is using the
``templates/djangocodemirror/include_field_bundles.html`` template.

Template tags
=============

For inputs
**********

You will need to load the template tags module in your templates like this : ::

    {% load djangocodemirror_inputs %}

Filters
-------

djangocodemirror_input_settings
    Get the generated widget settings and return it as JSON. It take the form field as required argument like this : ::

        {{ form.content|djangocodemirror_input_settings }}
djangocodemirror_init_input
    Return the HTML tag to embed the Javascript init for a djangocodemirror input field. Take the same argument as ``djangocodemirror_input_settings``.

For assets
**********

You will need to load the template tags module in your templates like this : ::

    {% load djangocodemirror_assets %}

Filters
-------

djangocodemirror_get_assets
    Return the html to load all needed assets for all given djangocodemirror fields

    This can only be used on a field that have allready been rendered.

    Usage : ::

        {% load djangocodemirror_assets %}

        <html>
            <head>
            ...
            {% djangocodemirror_get_assets form.myfield1 form.myfield2 %}
            </head>
        ...
        </html>

    Warning, the tag does not throw explicit template errors for invalid fields.
djangocodemirror_get_bundles
    It works exactly like the ``djangocodemirror_get_assets`` except it use django-assets
    bundles in place of direct assets. You should not use this if you don't have `django-assets`_
    installed.

Sample demonstration
====================

You can rapidly insert **Django-CodeMirror** in your project in adding
``djangocodemirror.urls`` to your project ``urls.py`` file. This will use
``djangocodemirror.views`` which contains the demonstration views.

::

    urlpatterns = patterns('',
        ...
        (r'^djangocodemirror-sample/', include('djangocodemirror.urls')),
        ...
    )

Three views are avalaible :

* The editor demonstration on ``djangocodemirror-sample/`` using `ReStructuredText`_;
* The preview view ``preview/`` used in editor demo, it require **sveedocuments** to
  work correctly or it will simply return a dummy content. This view accepts only
  **POST** request and return an empty response for all request type (like GET);
* The quicksave view ``quicksave/`` used in editor demo, doesn't really save anything,
  just do some validation. It require **sveedocuments** to work correctly.
* A public view ``settings/`` usable to edit some settings for the editor. These
  custom settings will be saved in a cookie.

The sample view uses the ``djangocodemirror/sample.html`` template that is using by
default the `Direct assets`_. If your project use `Bundle assets`_, you will have to
overload this template in your project by creating a ``djangocodemirror/sample.html``
template in your project templates directory and use the correct filter like this :

::

    {% extends "djangocodemirror/sample_base.html" %}
    {% load djangocodemirror_assets %}

    {% block djangocodemirror_assets_loading %}{% djangocodemirror_get_bundles form.content %}{% endblock %}


Internationalization and localization
=====================================

This application make usage of the `Django internationalization system`_ only in his
demonstration. However the editor is translated with his own system using a javascript
file for each available language.

To add a new language, you will have to add a new javascript file that will register the
new available language. Just create a file with this :

::

    DCM_Translations["NAME"] = {
        // Translations goes here
    };

Where ``NAME`` is the language locale name to register and ``// Translations goes here``
must be replaced by the content to translate. To see a full translation see the french
version in ``static/djangocodemirror/djangocodemirror.fr.js`` where you can see all the
string to translate.

You can save your file where you want in your project or application, you will just have
to register it in the setting `DJANGOCODEMIRROR_TRANSLATIONS`_.
