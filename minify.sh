#!/bin/bash

# To minify some static files

set -e

echo "Minifying CSS"
yui-compressor --type css -o djangocodemirror/static/djangocodemirror/djangocodemirror.min.css djangocodemirror/static/djangocodemirror/djangocodemirror.css
echo "Minifying JS"
yui-compressor --type js -o djangocodemirror/static/djangocodemirror/djangocodemirror.min.js djangocodemirror/static/djangocodemirror/djangocodemirror.js