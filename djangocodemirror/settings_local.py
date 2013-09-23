# -*- coding: utf-8 -*-
"""
App default settings
"""
from django.conf import settings

# HTML Code to insert for instanciate CodeMirror with a field
DJANGOCODEMIRROR_FIELD_INIT_JS = getattr(settings, 'DJANGOCODEMIRROR_FIELD_INIT_JS', u"""<script type="text/javascript">//<![CDATA[\njQuery(document).ready(function() {{ {inputid}_codemirror_instance = jQuery('#{inputid}').djangocodemirror({settings}); }});\n//]]></script>""")
CODEMIRROR_FIELD_INIT_JS = getattr(settings, 'CODEMIRROR_FIELD_INIT_JS', u"""<script type="text/javascript">//<![CDATA[\n{inputid}_codemirror_instance = CodeMirror.fromTextArea(document.getElementById('{inputid}'), {settings});\n//]]></script>""")

DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME = getattr(settings, 'DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME', "djangocodemirror_user_settings")
DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_MAXAGE = getattr(settings, 'SESSION_COOKIE_AGE', (60 * 60 * 24 * 7 * 8))

# The default path to use with the ``add_jquery`` widget argument
DEFAULT_JQUERY_PATH = "js/jquery/jquery.min.js"

# Default settings for CodeMirror
CODEMIRROR_SETTINGS = {
    'default': {
        'lineNumbers': True,
        'YouGotDefaultSettings': True,
        'mode': 'rst',
    },
    'djangocodemirror': {
        'mode': 'rst',
        'lineWrapping': True,
        'lineNumbers': True,
        'search_enabled': True,
    },
    'djangocodemirror_with_preview': {
        'mode': 'rst',
        'csrf': 'CSRFpass',
        'preview_url': '/preview/',
        'lineWrapping': True,
        'lineNumbers': True,
        'search_enabled': True,
    },
    'djangocodemirror_sample_demo': {
        'mode': 'rst',
        'csrf': 'CSRFpass',
        'settings_cookie': DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME,
        'preview_url': ('djangocodemirror-sample-preview', [], {}),
        'quicksave_url': ('djangocodemirror-sample-quicksave', [], {}),
        'settings_url': ('djangocodemirror-settings', [], {}),
        'lineWrapping': True,
        'lineNumbers': True,
        'search_enabled': True,
    },
}
CODEMIRROR_SETTINGS.update(getattr(settings, 'CODEMIRROR_SETTINGS', {}))

# Default setting key to use for DjangoCodeMirror field
DJANGOCODEMIRROR_DEFAULT_SETTING = getattr(settings, 'DJANGOCODEMIRROR_DEFAULT_SETTING', 'djangocodemirror')

# List of translations
DJANGOCODEMIRROR_TRANSLATIONS = getattr(settings, 'DJANGOCODEMIRROR_TRANSLATIONS', (
    ('djangocodemirror/djangocodemirror.fr.js'),
))

# Path to the buttons Javascript file
DJANGOCODEMIRROR_LIB_BUTTONS_PATH = getattr(settings, 'DJANGOCODEMIRROR_LIB_BUTTONS_PATH', 'djangocodemirror/buttons.js')
# Path to the syntax methods Javascript file
DJANGOCODEMIRROR_LIB_SYNTAX_METHODS_PATH = getattr(settings, 'DJANGOCODEMIRROR_LIB_SYNTAX_METHODS_PATH', 'djangocodemirror/syntax_methods.js')

# List of available CSS themes for CodeMirror
CODEMIRROR_THEMES = getattr(settings, 'CODEMIRROR_THEMES', (
    (u'Ambiance', 'CodeMirror/theme/ambiance.css'),
    (u'Eclipse', 'CodeMirror/theme/eclipse.css'),
    (u'Elegant', 'CodeMirror/theme/elegant.css'),
    (u'Lesser dark', 'CodeMirror/theme/lesser-dark.css'),
    (u'Neat', 'CodeMirror/theme/neat.css'),
    (u'Nice ambiance', 'djangocodemirror/theme/nice-ambiance.css'),
    (u'Nice Lesser dark', 'djangocodemirror/theme/nice-lesser-dark.css'),
))

# Default theme name used by DjangoCodeMirror
DJANGOCODEMIRROR_DEFAULT_THEME = getattr(settings, 'DJANGOCODEMIRROR_DEFAULT_THEME', 'Neat')

# List of available modes and their JavaScript file
CODEMIRROR_MODES = getattr(settings, 'CODEMIRROR_MODES', (
    (u'clike', u'CodeMirror/mode/clike/clike.js'),
    (u'clojure', u'CodeMirror/mode/clojure/clojure.js'),
    (u'coffeescript', u'CodeMirror/mode/coffeescript/coffeescript.js'),
    (u'css', u'CodeMirror/mode/css/css.js'),
    (u'diff', u'CodeMirror/mode/diff/diff.js'),
    (u'gfm', u'CodeMirror/mode/gfm/gfm.js'),
    (u'go', u'CodeMirror/mode/go/go.js'),
    (u'groovy', u'CodeMirror/mode/groovy/groovy.js'),
    (u'haskell', u'CodeMirror/mode/haskell/haskell.js'),
    (u'htmlembedded', u'CodeMirror/mode/htmlembedded/htmlembedded.js'),
    (u'htmlmixed', u'CodeMirror/mode/htmlmixed/htmlmixed.js'),
    (u'javascript', u'CodeMirror/mode/javascript/javascript.js'),
    (u'jinja2', u'CodeMirror/mode/jinja2/jinja2.js'),
    (u'less', u'CodeMirror/mode/less/less.js'),
    (u'lua', u'CodeMirror/mode/lua/lua.js'),
    (u'markdown', u'CodeMirror/mode/markdown/markdown.js'),
    (u'mysql', u'CodeMirror/mode/mysql/mysql.js'),
    (u'ntriples', u'CodeMirror/mode/ntriples/ntriples.js'),
    (u'pascal', u'CodeMirror/mode/pascal/pascal.js'),
    (u'perl', u'CodeMirror/mode/perl/perl.js'),
    (u'php', u'CodeMirror/mode/php/php.js'),
    (u'plsql', u'CodeMirror/mode/plsql/plsql.js'),
    (u'python', u'CodeMirror/mode/python/python.js'),
    (u'r', u'CodeMirror/mode/r/r.js'),
    (u'rst', u'CodeMirror/mode/rst/rst.js'),
    (u'ruby', u'CodeMirror/mode/ruby/ruby.js'),
    (u'rust', u'CodeMirror/mode/rust/rust.js'),
    (u'scheme', u'CodeMirror/mode/scheme/scheme.js'),
    (u'smalltalk', u'CodeMirror/mode/smalltalk/smalltalk.js'),
    (u'sparql', u'CodeMirror/mode/sparql/sparql.js'),
    (u'stex', u'CodeMirror/mode/stex/stex.js'),
    (u'tiddlywiki', u'CodeMirror/mode/tiddlywiki/tiddlywiki.js'),
    (u'velocity', u'CodeMirror/mode/velocity/velocity.js'),
    (u'verilog', u'CodeMirror/mode/verilog/verilog.js'),
    (u'xml', u'CodeMirror/mode/xml/xml.js'),
    (u'yaml', u'CodeMirror/mode/yaml/yaml.js'),
))

# Internal key names used for bundles
BUNDLES_CSS_NAME = "dcm-{settings_name}_css"
BUNDLES_JS_NAME = "dcm-{settings_name}_js"

# Option arguments use on the bundles
BUNDLES_CSS_OPTIONS = getattr(settings, 'BUNDLES_CSS_OPTIONS', {'filters':'yui_css', 'output':'css/dcm-{settings_name}.min.css'})
BUNDLES_JS_OPTIONS = getattr(settings, 'BUNDLES_JS_OPTIONS', {'filters':'yui_js', 'output':'js/dcm-{settings_name}.min.js'})
