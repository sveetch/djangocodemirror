/*
* Django-CodeMirror jQuery plugin
* 
* TODO: * CSS pour mettre une puce différente pour les liens internes et pour les liens externes;
*       * Ne pas déplacer le curseur après une insertion si il est déjà à la fin de la ligne;
*       * Améliorer le binding des touches de raccourcis clavier (utiliser l'api de codemirror?);
* 
* NOTE: Actual code doesn't pass yet the codemirror container instance to all core methods, so 
*       DjangoCodeMirror is compatible for multiple instances usage.
*/

/*
* CORE METHODS USED BY PLUGIN
*/
DCM_Core_Methods = {
    /*
    // Send a quick save request to the dedicated view
    */
    quicksave: function(button_instance, opts, djangocodemirror_container, codemirror_instance) {
        // If it's a string, assume that this is the variable name where there is the 
        // object {} to use
        if( jQuery.type(opts.quicksave_datas)=='string' ){
            try {
                opts.quicksave_datas = eval(opts.quicksave_datas);
            } catch (e) {
                opts.quicksave_datas = {};
            }
        }
        // Add current textarea content to the request args
        var thedatas = $.extend({}, opts.quicksave_datas, {
            "nocache": (new Date()).getTime(),
            "content": codemirror_instance.getValue()
        });
        // Do Ajax POST request to quicksave view
        $.ajax({
            type: 'POST',
            dataType: "json",
            global: false,
            url: opts.quicksave_url,
            data: thedatas,
            beforeSend: function(xhr, settings) {
                if(opts.csrf) {
                    eval(opts.csrf)(xhr, settings);
                }
            },
            success: function(data) {
                $(".DjangoCodeMirror_menu .buttonQuickSave", djangocodemirror_container).removeClass("ready");
                $(".DjangoCodeMirror_menu .buttonQuickSave", djangocodemirror_container).removeClass("error");
                if(data['status']=='form_invalid') {
                    $(".DjangoCodeMirror_menu .buttonQuickSave", djangocodemirror_container).addClass("error");
                    createGrowl(djangocodemirror_container, "warning", safegettext("Validation error"), data["errors"]["content"].join("<br/>"), false);
                } else {
                    createGrowl(djangocodemirror_container, "success", safegettext("Success"), safegettext("Successful save"), false);
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                // console.log(textStatus);
                // console.log(errorThrown);
                $(".DjangoCodeMirror_menu .buttonQuickSave", djangocodemirror_container).removeClass("ready");
                $(".DjangoCodeMirror_menu .buttonQuickSave", djangocodemirror_container).addClass("error");
                createGrowl(djangocodemirror_container, "warning", textStatus, errorThrown, false);
            }
        });
        return false;
    },
    /*
    // Maximize editor size
    */
    fullscreenEnter: function(button_instance, opts, djangocodemirror_container, codemirror_instance) {
        $("body","html").css({'height':"100%", 'width':"100%"});
        $("html").css('overflow',"hidden");
        
        djangocodemirror_container.addClass("fullScreen");
        // Build new scene where will be moved the editor in maximized size and add a 
        // empty container to mark the initial editor position
        var scene = $('<div>').attr('id', "DjangoCodeMirror_fullscreen_scene");
        var old_place_scene = $('<div>').attr('id', "DjangoCodeMirror_old_place");
        
        // Save initial editor size to restore after exiting the maximized mode
        $(".CodeMirror-scroll", djangocodemirror_container).data('original_size', $(".CodeMirror-scroll", djangocodemirror_container).height());
        
        // Catch and use the ESC key to exit from the maximized mode
        $(scene).keydown( function(e){
            if(e.keyCode == '27'){
                DCM_Core_Methods.fullscreenExit(opts, djangocodemirror_container, codemirror_instance);
                DCM_Core_Methods.closePreview(djangocodemirror_container, codemirror_instance);
                return false;
            }
            return true;
        });
        
        // Ajoute de la nouvelle scène dans le html à la fin du <body/> et déplace 
        // l'éditeur dedans
        djangocodemirror_container.after(old_place_scene);
        djangocodemirror_container.appendTo(scene);
        $("body").append(scene);
        
        // Calcul et applique les nouvelles dimensions
        var elems_css = DCM_Core_Methods.get_fullscreen_sizes(djangocodemirror_container, codemirror_instance);
        scene.css(elems_css[0]).attr('id', "DjangoCodeMirror_fullscreen_scene");
        djangocodemirror_container.css(
            "width",
            "100%"
        );
        // Met la hauteur de CodeMirror à la dimension qui lui est disponible
        $(".CodeMirror-scroll", djangocodemirror_container).css(elems_css[1]);
        DCM_Core_Methods.closePreview(djangocodemirror_container, codemirror_instance);
        // Recalcul auto de CodeMirror
        codemirror_instance.refresh();
    },
    /*
    // Exit maximized mode
    */
    fullscreenExit: function(button_instance, opts, djangocodemirror_container, codemirror_instance) {
        // Don't try to re-init all the thing if there are no displayed maximized editor
        if ($("#DjangoCodeMirror_fullscreen_scene").length==0){
            return;
        }
        djangocodemirror_container.removeClass("fullScreen");
        
        // Replace l'éditeur à son ancienne position (juste avant la balise dédiée à 
        // cet effet)
        $("#DjangoCodeMirror_old_place").before(djangocodemirror_container)
        $("#DjangoCodeMirror_old_place").remove();
        
        // Retire le hack anti-scroll et vire la scène fullscreen
        $("body","html").css({"height":'', "width":''});
        $("html").css("overflow", 'auto');
        $("#DjangoCodeMirror_fullscreen_scene").remove();
        
        // Restitue les dimensions originals
        djangocodemirror_container.css("width", '');
        $(".CodeMirror-scroll", djangocodemirror_container).css(
            "height",
            $(".CodeMirror-scroll", djangocodemirror_container).data('original_size') + "px"
        );
        DCM_Core_Methods.closePreview(djangocodemirror_container, codemirror_instance);
        codemirror_instance.refresh();
    },
    /*
    // undo/redo management
    */
    do_undo: function(button_instance, opts, djangocodemirror_container, codemirror_instance) {
        if(button_instance.hasClass("active")) {
            codemirror_instance.undo();
        }
    },
    do_redo: function(button_instance, opts, djangocodemirror_container, codemirror_instance) {
        if(button_instance.hasClass("active")){
            codemirror_instance.redo();
        }
    },
    /*
    // Send a preview request and display the rendered content
    */
    previewRender: function(djangocodemirror_settings, djangocodemirror_container, codemirror_instance) {
        // Don't add a new preview it if another one is allready displayed
        if (djangocodemirror_container.data("DCM_preview_markid")){
            return;
        }
        // Clean previous error markers
        $(".DjangoCodeMirror_tabs li.preview a .error", djangocodemirror_container).remove();
        // Do Ajax POST request to preview view
        $.ajax({
            type: 'POST',
            dataType: "html",
            global: false,
            url: djangocodemirror_settings.preview_url,
            data: {
                "nocache": (new Date()).getTime(),
                "content": codemirror_instance.getValue()
            },
            beforeSend: function(xhr, settings) {
                if(djangocodemirror_settings.csrf) {
                    eval(djangocodemirror_settings.csrf)(xhr, settings);
                }
            },
            success: function(data) {
                var elems_css = DCM_Core_Methods.get_preview_sizes(djangocodemirror_settings, djangocodemirror_container, codemirror_instance);
                // ID unique du conteneur de la preview à lier au conteneur de SPM
                var DCM_preview_id = "DCM_preview_id_"+$.now();
                djangocodemirror_container.data("DCM_preview_markid", DCM_preview_id);
                
                // Scène principal par dessus l'éditeur
                var scene = $('<div>').css(elems_css[0]);
                scene.addClass("DjangoCodeMirrorPreviewScene")
                scene.attr("id", DCM_preview_id);
                $("body").append(scene);
                
                // Conteneur de la preview renvoyée par le parser
                var content = $('<div>').css(elems_css[1]);
                content.addClass("PreviewContent")
                content.addClass("restructuredtext_container")
                scene.append(content);
                
                $(".DjangoCodeMirror_tabs li.editor", djangocodemirror_container).removeClass("tabactive");
                $(".DjangoCodeMirror_tabs li.preview", djangocodemirror_container).addClass("tabactive");
                // Ajout du contenu renvoyé par le parser
                content.append(data);
                // Contrôle du clic dans la preview, ouvre les liens dans une nouvelle 
                // fenêtre et bloque les ancres
                $('a', content).click(function () {
                    var url = $(this).attr('href');
                    var is_anchor = (url && url.indexOf('#')==0) ? true : false;
                    if(url && !is_anchor) {
                        window.open( url );
                    }
                    return false;
                });
            },
            error: function(jqXHR, textStatus, errorThrown) {
                $(".DjangoCodeMirror_tabs li.preview a", djangocodemirror_container).append('<span class="error"> (!)</span>');
            }
        });
        return false;
    },
    /*
    // Close preview display and get back to editor
    */
    closePreview: function(djangocodemirror_container, codemirror_instance) {
        // Don't add a new preview it if another one is allready displayed
        if (!djangocodemirror_container.data("DCM_preview_markid")){
            return;
        }
        $(".DjangoCodeMirror_tabs li.editor", djangocodemirror_container).addClass("tabactive");
        $(".DjangoCodeMirror_tabs li.preview", djangocodemirror_container).removeClass("tabactive");
        var DCM_preview_id = djangocodemirror_container.data("DCM_preview_markid");
        $("#"+DCM_preview_id).remove();
        djangocodemirror_container.removeData("DCM_preview_markid");
        codemirror_instance.focus();
    },
    /*
    // Getters to calculate CSS size of elements
    */
    get_preview_sizes: function(djangocodemirror_settings, djangocodemirror_container, codemirror_instance) {
        var editor_container = $(".CodeMirror-scroll", djangocodemirror_container);
        var menu_height = $(".DjangoCodeMirror_menu", djangocodemirror_container).outerHeight(true);
        var scene_css = {
            'position': "absolute",
            'z-index': 3000,
            'left': editor_container.offset().left,
            'top': editor_container.offset().top-menu_height,
            'width': editor_container.outerWidth()-(djangocodemirror_settings.preview_padding*2)-(djangocodemirror_settings.preview_borders*2),
            'height': editor_container.outerHeight()-(djangocodemirror_settings.preview_padding*2)+menu_height-(djangocodemirror_settings.preview_borders*2),
            'overflow': 'auto',
            'padding': djangocodemirror_settings.preview_padding
        };
        var content_css = {
            'width': editor_container.width()-(djangocodemirror_settings.preview_padding*4),
            'height': editor_container.height()-(djangocodemirror_settings.preview_padding*4),
            'border-size': 1
        };
        return [scene_css, content_css];
    },
    get_fullscreen_sizes: function(djangocodemirror_container, codemirror_instance) {
        var window_elem = $(window);
        var computed_margins = djangocodemirror_container.outerHeight(true) - $(".CodeMirror", djangocodemirror_container).outerHeight(true);
        var scene_css = {
            'position': "absolute",
            'z-index': 2000,
            'left': 0,
            'top': window_elem.scrollTop(),
            'width': window_elem.width(),
            'height': window_elem.height()
        };
        var content_css = {'height':(window_elem.height() - computed_margins) + "px"};
        return [scene_css, content_css];
    },
    /*
    / Save vertical scroll position from an element (the 'referer') in container element 
    / (the 'elem_container')
    */
    save_scroll_position: function(key, referer, elem_container) {
        if(referer == undefined){
            var elem_referer = $(window);
        } else {
            var elem_referer = referer;
        }
        if(elem_container == undefined) {
            elem_container = $('body');
        }
        var elem_container = $(elem_container);
        elem_container.data('DCM_'+key, elem_referer.scrollTop());
    },
    /*
    / Restore vertical scroll position from the given key in the 'elem_container' to the 
    / 'referer' element
    */
    restore_scroll_position: function(key, referer, elem_container) {
        if(referer == undefined){
            var elem_referer = $(window);
        } else {
            var elem_referer = referer;
        }
        if(elem_container == undefined) {
            elem_container = $('body');
        }
        var pos_data = elem_container.data('DCM_'+key);
        if(pos_data){
            elem_referer.scrollTop(pos_data);
            elem_container.removeData('DCM_'+key);
        }
    }
};


/*
* THE DJANGOCODEMIRROR JQUERY-PLUGIN
*/
(function($){$.fn.djangocodemirror = function(options) {
    var codemirror_instance = this;
    
    // Default for DjangoCodeMirror & CodeMirror
    var hlLine;
    var settings = $.extend( {
        'lineNumbers' : false,
        'onCursorActivity': function() {
            // TODO: this lack the container instance so this function is not multiple 
            //       instances compatible
            codemirror_instance.setLineClass(hlLine, null);
            var cur = codemirror_instance.getCursor();
            
            $(".DjangoCodeMirror_tabs .cursor_pos span.line").html((cur.line+1));
            $(".DjangoCodeMirror_tabs .cursor_pos span.ch").html((cur.ch+1));
            
            // Update the undo/redo buttons class from history items
            var histo = codemirror_instance.historySize();
            if(histo.undo>0) {
                $(".DjangoCodeMirror_menu .buttonUndo").addClass("active").removeClass("inactive");
            } else {
                $(".DjangoCodeMirror_menu .buttonUndo").addClass("inactive").removeClass("active");
            }
            if(histo.redo>0) {
                $(".DjangoCodeMirror_menu .buttonRedo").addClass("active").removeClass("inactive");
            } else {
                $(".DjangoCodeMirror_menu .buttonRedo").addClass("inactive").removeClass("active");
            }
            
            // Highlight active line
            hlLine = codemirror_instance.setLineClass(cur.line, "activeline");
        },
        // For DjangoCodeMirror only
        'fullscreen' : true,
        'help_link' : '',
        'quicksave_url' : '',
        'quicksave_datas' : {},
        //'enable_active_line' : false,
        'preview_url' : false,
        'csrf' : false,
        'undo_buttons' : true,
        'settings_cookie': '',
        'display_cursor_position': true,
        'preview_padding': 10,
        'no_tab_char': false,
        'preview_borders': 0
    }, options);
    // Default settings for buttons
    var default_button_settings = {
        'name' : '',
        'functype' : 'common',
        'method' : 'syntax',
        'classname' : '',
        'key' : false,
        'char' : false,
        'url' : false,
        'placeholder' : '',
        'begin_with' : false,
        'close_with' : false,
        'prompt' : false,
        'move_cursor_char' : 0,
        'separator' : false
    };
    // User settings in cookie
    if(settings.settings_cookie) {
        var cookie = $.cookies.get("djangocodemirror_user_settings");
        if(cookie){
            settings = $.extend( settings, cookie);
        }
    }
    
    // Build DjangoCodeMirror for each selected object
    this.each(function() {
        // DjangoCodeMirror global container
        var DCM_container = $("<div class=\"DjangoCodeMirror\"></div>");
        $(this).before(DCM_container);
        
        // Button bar container
        var header = $("<div class=\"DjangoCodeMirror_menu\"><ul></ul><div class=\"cale\"></div></div>");
        header.appendTo(DCM_container);
        
        // Moving textarea in the DjangoCodeMirror global container
        $(this).appendTo(DCM_container);
        
        // Tabs and status bar
        if(settings.preview_url || settings.display_cursor_position) {
            var footer = $("<div class=\"DjangoCodeMirror_tabs\"><ul></ul><div class=\"cale\"></div></div>");
            footer.appendTo(DCM_container);
            if(settings.preview_url) {
                var tab_preview_on = $("<li class=\"tab preview\"><a>"+safegettext("Preview")+"</a></li>");
                var tab_preview_off = $("<li class=\"tab editor tabactive\"><a>"+safegettext("Edit")+"</a></li>");
                tab_preview_off.appendTo(".DjangoCodeMirror_tabs ul", DCM_container);
                tab_preview_on.appendTo(".DjangoCodeMirror_tabs ul", DCM_container);
                tab_preview_on.on("click", function(event){
                    DCM_Core_Methods.previewRender(settings, DCM_container, codemirror_instance);
                });
                tab_preview_off.on("click", function(event){
                    DCM_Core_Methods.closePreview(DCM_container, codemirror_instance);
                });
            }
            if(settings.display_cursor_position) {
                $(".DjangoCodeMirror_tabs .cale", DCM_container).before("<div class=\"cursor_pos\">"+safegettext("Line")+"&nbsp;:&nbsp;<span class=\"line\">1</span> &nbsp;&nbsp; "+safegettext("Col")+"&nbsp;:&nbsp;<span class=\"ch\">1</span></div>");
            }
        }
        
        // Build CodeMirror
        codemirror_instance = CodeMirror.fromTextArea(this, settings);
        // Force options in codemirror that it doesn't know of
        codemirror_instance.setOption('no_tab_char', settings.no_tab_char);
        codemirror_instance.setOption('extraKeys', {
            "Tab": tab_transformer,
            // TODO: Ctrl/Cmd prefix should be determined from the enabled default keymap
            "Ctrl-S": function(cm){ cm.save(); $('.buttonQuickSave').trigger('click'); }
            // TODO: Here should be defined syntax button keybinding from there key attribute
        });
        
        // Buttons bar
        _buttons_preprocessing(settings, default_button_settings);
        $.each(DCM_Buttons_settings, function(item_index, item_value) {
            if(item_value) {
                var item_settings = $.extend({}, default_button_settings, item_value);
                // Add entry to bar
                if(item_settings.separator) {
                    _add_bar_separator(DCM_container);
                } else {
                    _add_bar_button(item_settings, DCM_container, codemirror_instance);
                }
            }
        });
        
        $(window).bind('resize', function(event){
            resize(settings, DCM_container, codemirror_instance);
        });
        
        // Default active line
        // TODO: should be optional on settings
        hlLine = codemirror_instance.setLineClass(0, "activeline");
        
        // Refresh update of CodeMirror
        codemirror_instance.refresh();
    });
    
    /*
    * Transform tabulation character in spaces
    */
    function tab_transformer(cm) {
        var tab = "\t";
        if(cm.getOption('no_tab_char')) {
            tab = "";
            for (var l=0; l < cm.getOption('tabSize'); l++) {
                tab += " ";
            }
        }
        cm.replaceSelection(tab, "end");
    };
    
    /*
    * Pre-processing on avalaible buttons
    * 
    * This is where buttons should be deleted or modified from defined settings
    */
    function _buttons_preprocessing(global_settings, default_settings) {
        // Available buttons indexation on classname
        var button_indexes = {};
        $.each(DCM_Buttons_settings, function(item_index, item_value) {
            if(!item_value.separator){
                button_indexes[item_value.classname] = item_index;
            }
        });
        
        // Delete button from registry if option is disabled
        // Assume that there are two buttons followed by a separator
        if( button_indexes['buttonFullscreenEnter'] != undefined && button_indexes['buttonFullscreenEnter'] != null){
            if(!global_settings.fullscreen){
                var pos_enter = button_indexes['buttonFullscreenEnter'];
                var pos_exit = button_indexes['buttonFullscreenExit'];
                delete DCM_Buttons_settings[pos_enter];
                delete DCM_Buttons_settings[pos_exit];
                if(DCM_Buttons_settings[pos_exit+1].separator) {
                    delete DCM_Buttons_settings[pos_exit+1];
                }
            }
        }

        // Quicksave button
        if( button_indexes['buttonQuickSave'] != undefined && button_indexes['buttonQuickSave'] != null){
            var pos = button_indexes['buttonQuickSave'];
            if(global_settings.quicksave_url){
                DCM_Buttons_settings[pos].quicksave_url = global_settings.quicksave_url;
                DCM_Buttons_settings[pos].quicksave_datas = global_settings.quicksave_datas;
                DCM_Buttons_settings[pos].csrf = global_settings.csrf;
            } else {
                delete DCM_Buttons_settings[pos];
                if(DCM_Buttons_settings[pos+1].separator) {
                    delete DCM_Buttons_settings[pos+1];
                }
            }
        }
        
        // Undo/Redo buttons
        // Assume that there are two buttons followed by a separator
        if( button_indexes['buttonUndo'] != undefined && button_indexes['buttonUndo'] != null){
            var pos_undo = button_indexes['buttonUndo'];
            var pos_redo = button_indexes['buttonRedo'];
            if(!global_settings.undo_buttons){
                delete DCM_Buttons_settings[pos_undo];
                delete DCM_Buttons_settings[pos_redo];
                if(DCM_Buttons_settings[pos_redo+1].separator) {
                    delete DCM_Buttons_settings[pos_redo+1];
                }
            }
        }
        
        // Help link if setted
        if( button_indexes['buttonHelp'] != undefined && button_indexes['buttonHelp'] != null){
            var pos = button_indexes['buttonHelp'];
            if( global_settings.help_link ){
                DCM_Buttons_settings[pos].url = global_settings.help_link;
            } else {
                delete DCM_Buttons_settings[pos];
            }
        }
    };
    
    /*
    * Add separator in buttons bar 
    */
    function _add_bar_separator(container, direction) {
        if(!direction || direction=='horizontal') {
            $('<li class="separator horizontal">-----</li>').appendTo('.DjangoCodeMirror_menu ul', container);
        } else {
            $('<li class="separator vertical">-----</li>').appendTo('.DjangoCodeMirror_menu ul', container);
        }
    };
    
    /*
    * Add button to the bar
    */
    function _add_bar_button(item_opts, container, codemirror_instance) {
        var accesskey = (item_opts.key) ? ' accesskey="'+item_opts.key+'"' : '';
        var button = $('<li class="button '+item_opts.classname+'"><a'+accesskey+' title="'+safegettext(item_opts.name)+'">'+safegettext(item_opts.name)+'</a></li>')
        button.appendTo('.DjangoCodeMirror_menu ul', container);
        button.on("click", item_opts, function(event){
            var opts = event.data;
            if(opts.placeholder) {
                opts.placeholder = safegettext(opts.placeholder);
            }
            // Get the content value if not empty, else use the placeholder value
            var value = codemirror_instance.getSelection()||opts.placeholder;
            // Evaluate method
            if(opts.functype == 'fullscreenEnter' || opts.functype == 'fullscreenExit' || opts.functype == 'quicksave'
                 || opts.functype == 'do_undo' || opts.functype == 'do_redo') {
                eval("DCM_Core_Methods."+opts.functype)(button, opts, container, codemirror_instance);
            } else {
                eval("DCM_Syntax_Methods."+opts.functype)(value, codemirror_instance, opts);
                // Try to put cursor after the updated content, seems a little buggy
                var pos = codemirror_instance.getCursor();
                pos.ch += 1;
                codemirror_instance.setCursor(pos);
            }
            // Restore focus after action
            codemirror_instance.focus();
        });
    };
    
    /*
    * Resize method to use when the editor window is resized
    */
    function resize(djangocodemirror_settings, djangocodemirror_container, codemirror_instance) {
        // For Maximize mode
        if ($("#DjangoCodeMirror_fullscreen_scene").length>0){
            var elems_css = DCM_Core_Methods.get_fullscreen_sizes(djangocodemirror_container, codemirror_instance);
            $("#DjangoCodeMirror_fullscreen_scene").css(elems_css[0]);
            $(".CodeMirror-scroll", djangocodemirror_container).css(elems_css[1]);
        }
        // For preview display
        var DCM_preview_id = djangocodemirror_container.data("DCM_preview_markid");
        if (DCM_preview_id){
            var elems_css = DCM_Core_Methods.get_preview_sizes(djangocodemirror_settings, djangocodemirror_container, codemirror_instance);
            var editor_container = $(".CodeMirror-scroll", djangocodemirror_container);
            $("#"+DCM_preview_id).css(elems_css[0]);
            $("#"+DCM_preview_id+" .PreviewContent").css(elems_css[1]);
        }
        codemirror_instance.refresh();
    };
    
    return codemirror_instance;
};})( jQuery );