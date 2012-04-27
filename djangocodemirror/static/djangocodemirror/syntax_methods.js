/*
* Syntax methods used by DjangoCodeMirror buttons
*/
DCM_Syntax_Methods = {
    /*
    // Common element embrace
    */
    common: function(value, codemirror_instance, opts) {
        codemirror_instance.replaceSelection(opts.begin_with + value + opts.close_with);
    },
    /*
    // Link
    */
    link: function(value, codemirror_instance, opts) {
        var url = prompt(safegettext("Link"),"http://");
        if(url){
            codemirror_instance.replaceSelection('`'+ value +' <'+ url +'>`_');
        }
    },
    /*
    // Link
    */
    externalressource: function(value, codemirror_instance, opts) {
        if(opts['url']){
            window.open( opts['url'] );
        }
    },
    /*
    // Header formating
    */
    title: function(value, codemirror_instance, opts) {
        var heading = '';
        for(i = 0; i < value.length; i++) {
            heading += opts.char;
        }
        codemirror_instance.replaceSelection(value+'\n'+heading+'\n');
    },
    /*
    // Cite
    */
    cite: function(value, codemirror_instance, opts) {
        codemirror_instance.replaceSelection(DCM_Syntax_Methods._indenter(value, opts.begin_with));
    },
    /*
    // Bullet list
    */
    bulletlist: function(value, codemirror_instance, opts) {
        codemirror_instance.replaceSelection(DCM_Syntax_Methods._indenter(value, '* ')+'\n');
    },
    /*
    // Numbered list
    */
    numberedlist: function(value, codemirror_instance, opts) {
        codemirror_instance.replaceSelection(DCM_Syntax_Methods._indenter(value, '#. ')+'\n');
    },
    /*
    // Source content formating
    */
    sourcecode: function(value, codemirror_instance, opts) {
        var lexer_name = prompt(safegettext("Language name"),"");
        if(lexer_name){
            var directive_head = "..  sourcecode:: "+lexer_name+"\n    :linenos:\n\n";
            codemirror_instance.replaceSelection(directive_head+DCM_Syntax_Methods._indenter(value, '    '));
        }
    },
    /*
    // Indent content
    */
    _indenter: function(content, indent) {
        if(!indent){
            indent = "    ";
        }
        var lines = content.split(/\r?\n/), blocks = [];
        for (var l=0; l < lines.length; l++) {
            blocks.push(indent+lines[l]);
        }
        return blocks.join("\n");
    }
};