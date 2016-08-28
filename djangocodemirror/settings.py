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

# Javascript base files for CodeMirror, they will be loaded before every other CodeMirror Javascript components.
CODEMIRROR_BASE_JS = ["CodeMirror/lib/codemirror.js"]

# CSS base files for CodeMirror, they will be loaded before every other CodeMirror CSS components.
CODEMIRROR_BASE_CSS = ["CodeMirror/lib/codemirror.css"]

# Available CodeMirror CSS theme files
CODEMIRROR_THEMES = {
    'ambiance': 'CodeMirror/theme/ambiance.css',
    'eclipse': 'CodeMirror/theme/eclipse.css',
    'elegant': 'CodeMirror/theme/elegant.css',
    'lesser_dark': 'CodeMirror/theme/lesser-dark.css',
    'neat': 'CodeMirror/theme/neat.css',
    'nice_ambiance': 'djangocodemirror/theme/nice-ambiance.css',
    'nice_lesser_dark': 'djangocodemirror/theme/nice-lesser-dark.css',
}

# Available CodeMirror Javascript mode files
CODEMIRROR_MODES = {
    'clike': 'CodeMirror/mode/clike/clike.js',
    'clojure': 'CodeMirror/mode/clojure/clojure.js',
    'coffeescript': 'CodeMirror/mode/coffeescript/coffeescript.js',
    'css': 'CodeMirror/mode/css/css.js',
    'diff': 'CodeMirror/mode/diff/diff.js',
    'gfm': 'CodeMirror/mode/gfm/gfm.js',
    'go': 'CodeMirror/mode/go/go.js',
    'groovy': 'CodeMirror/mode/groovy/groovy.js',
    'haskell': 'CodeMirror/mode/haskell/haskell.js',
    'htmlembedded': 'CodeMirror/mode/htmlembedded/htmlembedded.js',
    'htmlmixed': 'CodeMirror/mode/htmlmixed/htmlmixed.js',
    'javascript': 'CodeMirror/mode/javascript/javascript.js',
    'jinja2': 'CodeMirror/mode/jinja2/jinja2.js',
    'less': 'CodeMirror/mode/less/less.js',
    'lua': 'CodeMirror/mode/lua/lua.js',
    'markdown': 'CodeMirror/mode/markdown/markdown.js',
    'mysql': 'CodeMirror/mode/mysql/mysql.js',
    'ntriples': 'CodeMirror/mode/ntriples/ntriples.js',
    'pascal': 'CodeMirror/mode/pascal/pascal.js',
    'perl': 'CodeMirror/mode/perl/perl.js',
    'php': 'CodeMirror/mode/php/php.js',
    'plsql': 'CodeMirror/mode/plsql/plsql.js',
    'python': 'CodeMirror/mode/python/python.js',
    'r': 'CodeMirror/mode/r/r.js',
    'rst': 'CodeMirror/mode/rst/rst.js',
    'ruby': 'CodeMirror/mode/ruby/ruby.js',
    'rust': 'CodeMirror/mode/rust/rust.js',
    'scheme': 'CodeMirror/mode/scheme/scheme.js',
    'smalltalk': 'CodeMirror/mode/smalltalk/smalltalk.js',
    'sparql': 'CodeMirror/mode/sparql/sparql.js',
    'stex': 'CodeMirror/mode/stex/stex.js',
    'tiddlywiki': 'CodeMirror/mode/tiddlywiki/tiddlywiki.js',
    'velocity': 'CodeMirror/mode/velocity/velocity.js',
    'verilog': 'CodeMirror/mode/verilog/verilog.js',
    'xml': 'CodeMirror/mode/xml/xml.js',
    'yaml': 'CodeMirror/mode/yaml/yaml.js',
}

# Internal key names used for bundles
CODEMIRROR_BUNDLES_CSS_NAME = "dcm-{settings_name}_css"
CODEMIRROR_BUNDLES_JS_NAME = "dcm-{settings_name}_js"

# Option arguments use on the bundles
CODEMIRROR_BUNDLES_CSS_OPTIONS = {
    'filters':'yui_css',
    'output':'css/dcm-{settings_name}.min.css',
}
CODEMIRROR_BUNDLES_JS_OPTIONS = {
    'filters':'yui_js',
    'output':'js/dcm-{settings_name}.min.js',
}
