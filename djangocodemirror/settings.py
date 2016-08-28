# -*- coding: utf-8 -*-
"""
Default app settings
"""
# HTML Code to insert for instanciate CodeMirror with a field
CODEMIRROR_FIELD_INIT_JS = ("""<script type="text/javascript">"""
    """//<![CDATA[\n{inputid}_codemirror_instance = """
    """CodeMirror.fromTextArea(document.getElementById('{inputid}'), """
    """{settings});\n//]]></script>""")

# Default settings for CodeMirror
CODEMIRROR_SETTINGS = {
    'rst-editor': {
        'mode': 'rst',
        'lineWrapping': True,
        'lineNumbers': True,
    },
}

# List of available CSS themes for CodeMirror
CODEMIRROR_THEMES = (
    (u'Ambiance', 'CodeMirror/theme/ambiance.css'),
    (u'Eclipse', 'CodeMirror/theme/eclipse.css'),
    (u'Elegant', 'CodeMirror/theme/elegant.css'),
    (u'Lesser dark', 'CodeMirror/theme/lesser-dark.css'),
    (u'Neat', 'CodeMirror/theme/neat.css'),
    (u'Nice ambiance', 'djangocodemirror/theme/nice-ambiance.css'),
    (u'Nice Lesser dark', 'djangocodemirror/theme/nice-lesser-dark.css'),
)

# List of available modes and their JavaScript file
CODEMIRROR_MODES = (
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
)

# Internal key names used for bundles
BUNDLES_CSS_NAME = "dcm-{settings_name}_css"
BUNDLES_JS_NAME = "dcm-{settings_name}_js"

# Option arguments use on the bundles
BUNDLES_CSS_OPTIONS = {
    'filters':'yui_css',
    'output':'css/dcm-{settings_name}.min.css',
}
BUNDLES_JS_OPTIONS = {
    'filters':'yui_js',
    'output':'js/dcm-{settings_name}.min.js',
}
