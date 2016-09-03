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
        'mode': 'reStructuredText',
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
# TODO: This is wrong because collected mode name is a display name, not the
# used keyword by Codemirror to retrieve the mode file (seems its relative dir
# name instead).
CODEMIRROR_MODES = {
    "C": "CodeMirror/mode/c/c.js",
    "C++": "CodeMirror/mode/c++/c++.js",
    "CSS": "CodeMirror/mode/css/css.js",
    "CoffeeScript": "CodeMirror/mode/coffeescript/coffeescript.js",
    "Django": "CodeMirror/mode/django/django.js",
    "Dockerfile": "CodeMirror/mode/dockerfile/dockerfile.js",
    "HTML": "CodeMirror/mode/html/html.js",
    "JSON": "CodeMirror/mode/json/json.js",
    "Java": "CodeMirror/mode/java/java.js",
    "JavaScript": "CodeMirror/mode/javascript/javascript.js",
    "Jinja2": "CodeMirror/mode/jinja2/jinja2.js",
    "LESS": "CodeMirror/mode/less/less.js",
    "LaTeX": "CodeMirror/mode/latex/latex.js",
    "Markdown": "CodeMirror/mode/markdown/markdown.js",
    "PHP": "CodeMirror/mode/php/php.js",
    "Perl": "CodeMirror/mode/perl/perl.js",
    "Python": "CodeMirror/mode/python/python.js",
    "SCSS": "CodeMirror/mode/scss/scss.js",
    "SQL": "CodeMirror/mode/sql/sql.js",
    "reStructuredText": "CodeMirror/mode/restructuredtext/restructuredtext.js",
    "Sass": "CodeMirror/mode/sass/sass.js",
    "Shell": "CodeMirror/mode/shell/shell.js",
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
