# -*- coding: utf-8 -*-
"""
Default app settings
====================

"""
#: HTML Code to instanciate CodeMirror for a field
CODEMIRROR_FIELD_INIT_JS = ("""<script>var {inputid}_codemirror = """
                            """CodeMirror.fromTextArea("""
                            """document.getElementById("{inputid}"),"""
                            """{settings});</script>""")


#: Default settings for CodeMirror
CODEMIRROR_SETTINGS = {
    'empty': {},
    'rst-editor': {
        'mode': 'rst',
        'lineWrapping': True,
        'lineNumbers': True,
    },
}

#: Javascript base files for CodeMirror, they will be loaded before every other
#: CodeMirror Javascript components.
CODEMIRROR_BASE_JS = ["CodeMirror/lib/codemirror.js"]

#: CSS base files for CodeMirror, they will be loaded before every other
#: CodeMirror CSS components.
CODEMIRROR_BASE_CSS = ["CodeMirror/lib/codemirror.css"]

#: Available CodeMirror CSS theme files, this is only a subset of available
#: themes
CODEMIRROR_THEMES = {
    "ambiance": "CodeMirror/theme/ambiance.css",
    "ambiance-mobile": "CodeMirror/theme/ambiance-mobile.css",
    "base16-dark": "CodeMirror/theme/base16-dark.css",
    "bespin": "CodeMirror/theme/bespin.css",
    "dracula": "CodeMirror/theme/dracula.css",
    "eclipse": "CodeMirror/theme/eclipse.css",
    "elegant": "CodeMirror/theme/elegant.css",
    "neat": "CodeMirror/theme/neat.css",
    "neo": "CodeMirror/theme/neo.css",
    "night": "CodeMirror/theme/night.css",
    "panda-syntax": "CodeMirror/theme/panda-syntax.css",
    "xq-light": "CodeMirror/theme/xq-light.css",
    "yeti": "CodeMirror/theme/yeti.css",
    "zenburn": "CodeMirror/theme/zenburn.css",
}

#: Available CodeMirror Javascript mode files, this is only a subset of
#: available modes
CODEMIRROR_MODES = {
    "css": "CodeMirror/mode/css/css.js",
    "django": "CodeMirror/mode/django/django.js",
    "html": "CodeMirror/mode/html/html.js",
    "json": "CodeMirror/mode/json/json.js",
    "javascript": "CodeMirror/mode/javascript/javascript.js",
    "markdown": "CodeMirror/mode/markdown/markdown.js",
    "php": "CodeMirror/mode/php/php.js",
    "perl": "CodeMirror/mode/perl/perl.js",
    "python": "CodeMirror/mode/python/python.js",
    "scss": "CodeMirror/mode/scss/scss.js",
    "rst": "CodeMirror/mode/restructuredtext/restructuredtext.js",
    "shell": "CodeMirror/mode/shell/shell.js",
}

#: Key name template used for Javascript bundles
CODEMIRROR_BUNDLE_CSS_NAME = "dcm-{settings_name}_css"

#: Key name template used for CSS bundles
CODEMIRROR_BUNDLE_JS_NAME = "dcm-{settings_name}_js"

#: Option arguments used for CSS bundles
CODEMIRROR_BUNDLE_CSS_OPTIONS = {
    'filters':'yui_css',
    'output':'css/dcm-{settings_name}.min.css',
}

#: Option arguments used for Javascript bundles
CODEMIRROR_BUNDLE_JS_OPTIONS = {
    'filters':'yui_js',
    'output':'js/dcm-{settings_name}.min.js',
}
