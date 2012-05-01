# -*- coding: utf-8 -*-
"""
App default settings
"""
from django.conf import settings

# HTML Code to insert for instanciate CodeMirror with a field
DJANGOCODEMIRROR_FIELD_INIT_JS = getattr(settings, 'DJANGOCODEMIRROR_FIELD_INIT_JS', u"""<script language="JavaScript" type="text/javascript">//<![CDATA[\n$(document).ready(function() {{ {inputid}_codemirror_instance = $('#{inputid}').djangocodemirror({settings}); }});\n//]]></script>""")
CODEMIRROR_FIELD_INIT_JS = getattr(settings, 'CODEMIRROR_FIELD_INIT_JS', u"""<script language="JavaScript" type="text/javascript">//<![CDATA[\n{inputid}_codemirror_instance = CodeMirror.fromTextArea(document.getElementById('{inputid}'), {settings});\n//]]></script>""")

DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME = getattr(settings, 'DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME', "djangocodemirror_user_settings")
DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_MAXAGE = getattr(settings, 'SESSION_COOKIE_AGE', (60 * 60 * 24 * 7 * 8))

# Default settings for CodeMirror
CODEMIRROR_SETTINGS = {
    'default': {
        'lineNumbers': True,
    },
    'djangocodemirror': {
        'mode': 'rst',
        'lineWrapping': False,
        'lineNumbers': True,
        'search_enabled': True,
    },
    'djangocodemirror_with_preview': {
        'mode': 'rst',
        'csrf': 'CSRFpass',
        'preview_url': '/preview/',
        'lineWrapping': False,
        'lineNumbers': True,
        'search_enabled': True,
    },
    'djangocodemirror_sample_demo': {
        'mode': 'rst',
        'csrf': 'CSRFpass',
        'settings_cookie': DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME,
        'preview_url': ('djangocodemirror-sample-preview', [], {}),
        'quicksave_url': ('djangocodemirror-sample-quicksave', [], {}),
        'lineWrapping': False,
        'lineNumbers': True,
        'search_enabled': True,
    },
}
CODEMIRROR_SETTINGS.update(getattr(settings, 'CODEMIRROR_SETTINGS', {}))

# Default setting key to use for DjangoCodeMirror
DJANGOCODEMIRROR_DEFAULT_SETTING = getattr(settings, 'DJANGOCODEMIRROR_DEFAULT_SETTING', 'djangocodemirror')

# Relative paths for widget medias (CSS, JS)
CODEMIRROR_ROOT = getattr(settings, 'CODEMIRROR_ROOT', 'CodeMirror/') # TODO: Implement usage for settings below
JQUERY_PLUGINS_ROOT = getattr(settings, 'JQUERY_PLUGINS_ROOT', 'jquery/plugins/') # TODO: Implement usage for settings below

CODEMIRROR_FILEPATH_LIB = getattr(settings, 'CODEMIRROR_FILEPATH_LIB', 'CodeMirror/lib/codemirror.js')
CODEMIRROR_FILEPATH_CSS = getattr(settings, 'CODEMIRROR_FILEPATH_CSS', 'CodeMirror/lib/codemirror.css')
CODEMIRROR_FILEPATH_DIALOG_LIB = getattr(settings, 'CODEMIRROR_FILEPATH_DIALOG_LIB', 'CodeMirror/lib/util/dialog.js')
CODEMIRROR_FILEPATH_DIALOG_CSS = getattr(settings, 'CODEMIRROR_FILEPATH_DIALOG_CSS', 'CodeMirror/lib/util/dialog.css')
CODEMIRROR_FILEPATH_SEARCH_LIB = getattr(settings, 'CODEMIRROR_FILEPATH_SEARCH_LIB', 'CodeMirror/lib/util/search.js')
CODEMIRROR_FILEPATH_SEARCHCURSOR_LIB = getattr(settings, 'CODEMIRROR_FILEPATH_SEARCHCURSOR_LIB', 'CodeMirror/lib/util/searchcursor.js')

DJANGOCODEMIRROR_FILEPATH_LIB = getattr(settings, 'DJANGOCODEMIRROR_FILEPATH_LIB', 'djangocodemirror/djangocodemirror.js')
DJANGOCODEMIRROR_FILEPATH_TRANSLATION = getattr(settings, 'DJANGOCODEMIRROR_FILEPATH_TRANSLATION', 'djangocodemirror/djangocodemirror.translation.js')
DJANGOCODEMIRROR_FILEPATH_CSS = getattr(settings, 'DJANGOCODEMIRROR_FILEPATH_CSS', 'djangocodemirror/djangocodemirror.css')
DJANGOCODEMIRROR_FILEPATH_BUTTONS = getattr(settings, 'DJANGOCODEMIRROR_FILEPATH_BUTTONS', 'djangocodemirror/buttons.js')
DJANGOCODEMIRROR_FILEPATH_METHODS = getattr(settings, 'DJANGOCODEMIRROR_FILEPATH_METHODS', 'djangocodemirror/syntax_methods.js')
DJANGOCODEMIRROR_FILEPATH_CONSOLE = getattr(settings, 'DJANGOCODEMIRROR_FILEPATH_CONSOLE', 'djangocodemirror/qtip_console.js')
DJANGOCODEMIRROR_FILEPATH_CSRF = getattr(settings, 'DJANGOCODEMIRROR_FILEPATH_CSRF', 'djangocodemirror/csrf.js')
DJANGOCODEMIRROR_FILEPATH_COOKIES = getattr(settings, 'DJANGOCODEMIRROR_FILEPATH_COOKIES', 'jquery/plugins/jquery.cookies.2.2.0.min.js')

QTIP_FILEPATH_LIB = getattr(settings, 'QTIP_FILEPATH_LIB', 'jquery/plugins/qtip/jquery.qtip.min.js')
QTIP_FILEPATH_CSS = getattr(settings, 'QTIP_FILEPATH_CSS', 'jquery/plugins/qtip/jquery.qtip.min.css')

# List of translations
DJANGOCODEMIRROR_TRANSLATIONS = getattr(settings, 'DJANGOCODEMIRROR_TRANSLATIONS', (
    ('djangocodemirror/djangocodemirror.fr.js'),
))

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
    (u'rpm', u'CodeMirror/mode/rpm/rpm.js'),
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
    (u'xmlpure', u'CodeMirror/mode/xmlpure/xmlpure.js'),
    (u'yaml', u'CodeMirror/mode/yaml/yaml.js'),
))