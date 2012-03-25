/*
* Plugin d'initialisation de "CodeMirror" et ajout autour d'une interface 
* d'enrichissement qu'on apellera "DjangoCodeMirror" (par pure modestie..) qui ajoute des 
* boutons d'aides à la syntaxe ReST, fullscreen et preview. Le multi-instances de 
* DjangoCodeMirror est supporté.
* 
* TODO: * CSS pour mettre une puce différente pour les liens internes et pour les liens externes;
*       * Boutons pour appliquer le undo/redo (mais sans ajout de raccourcis clavier);
*       * Activation des modes de recherches et remplacement de CodeMirror;
*       * Déplacer les chaînes de texte dans un fichier séparé pour pouvoir faire des traductions par i18n;
*       * Ne pas déplacer le curseur après une insertion si il est déjà à la fin de la ligne;
*       * Améliorer le binding des touches de raccourcis clavier (utiliser l'api de codemirror?);
*/

/*
* CORE METHODS USED BY PLUGIN
*/
DCM_Core_Methods = {
    /*
    // Ouverture du mode FULLSCREEN
    */
    quicksave: function(opts, djangocodemirror_container, codemirror_instance) {
        // Une chaine de caractère implique un nom de variable à utiliser qui contient 
        // l'objet {} à utiliser
        if( jQuery.type(opts.quicksave_datas)=='string' ){
            try {
                opts.quicksave_datas = eval(opts.quicksave_datas);
            } catch (e) {
                opts.quicksave_datas = {};
            }
        }
        // Données à envoyer, ajoute le contenu extrait du textarea
        var thedatas = $.extend({}, opts.quicksave_datas, {
            "nocache": (new Date()).getTime(),
            "content": codemirror_instance.getValue()
        });
        // Requête
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
                    createGrowl(djangocodemirror_container, "warning", "Erreur de validation", data["errors"]["content"].join("<br/>"), false);
                } else {
                    createGrowl(djangocodemirror_container, "success", "Succès", "Sauvegarde réussie", false);
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.log(textStatus);
                console.log(errorThrown);
                $(".DjangoCodeMirror_menu .buttonQuickSave", djangocodemirror_container).removeClass("ready");
                $(".DjangoCodeMirror_menu .buttonQuickSave", djangocodemirror_container).addClass("error");
                createGrowl(djangocodemirror_container, "warning", textStatus, errorThrown, false);
            }
        });
        return false;
    },
    /*
    // Ouverture du mode FULLSCREEN
    */
    fullscreenEnter: function(opts, djangocodemirror_container, codemirror_instance) {
        $("body","html").css({'height':"100%", 'width':"100%"});
        $("html").css('overflow',"hidden");
        
        djangocodemirror_container.addClass("fullScreen");
        // Prépare la nouvelle scène de l'éditeur
        var scene = $('<div>').attr('id', "DjangoCodeMirror_fullscreen_scene");
        var old_place_scene = $('<div>').attr('id', "DjangoCodeMirror_old_place");
        
        // Sauvegarde la dimension originale du textarea pour sa restitution 
        // à la sortie du fullscreen
        $(".CodeMirror-scroll", djangocodemirror_container).data('original_size', $(".CodeMirror-scroll", djangocodemirror_container).height());
        
        // Contrôle de la touche ESC pour fermer l'éditeur
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
    // Fermeture du mode FULLSCREEN
    */
    fullscreenExit: function(opts, djangocodemirror_container, codemirror_instance) {
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
    // Gestion de l'affichage de la PREVIEW
    */
    previewRender: function(djangocodemirror_settings, djangocodemirror_container, codemirror_instance) {
        // Vire un éventuel signal d'erreur d'une requête précédente
        $(".DjangoCodeMirror_tabs li.preview a .error", djangocodemirror_container).remove();
        // Requête
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
    // Fermeture du mode FULLSCREEN
    */
    closePreview: function(djangocodemirror_container, codemirror_instance) {
        $(".DjangoCodeMirror_tabs li.editor", djangocodemirror_container).addClass("tabactive");
        $(".DjangoCodeMirror_tabs li.preview", djangocodemirror_container).removeClass("tabactive");
        var DCM_preview_id = djangocodemirror_container.data("DCM_preview_markid");
        $("#"+DCM_preview_id).remove();
        djangocodemirror_container.removeData("DCM_preview_markid");
    },
    /*
    // Getters pour calculer les css des éléments principaux
    */
    get_preview_sizes: function(djangocodemirror_settings, djangocodemirror_container, codemirror_instance) {
        // Récupère le conteneur en cours de l'éditeur
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
    / Sauvegarde une la position verticale d'une référence
    / La valeur est stockée sous le nom 'DCM_'+key dans le container 
    / spécifié (si non spécifié, sur le <body/> par défaut)
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
    / Restauration de la position verticale enregistrée d'un élément (referer)
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
            codemirror_instance.setLineClass(hlLine, null);
            hlLine = codemirror_instance.setLineClass(codemirror_instance.getCursor().line, "activeline");
        },
        // For DjangoCodeMirror only
        'fullscreen' : true,
        'help_link' : '',
        'quicksave_url' : '',
        'quicksave_datas' : {},
        'preview_url' : false,
        'csrf' : false,
        'preview_padding': 10,
        'preview_borders': 0
    }, options);
    // Default settings for buttons
    var default_button_settings = {
        'name' : '',
        'functype' : 'common',
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
    
    // En mode normal, on initialise l'interface de DjangoCodeMirror puis on y déplace 
    // le textarea visé et enfin on initialise CodeMirror qui va s'y intégrer
    this.each(function() {
        // Conteneur principal de DjangoCodeMirror
        var DCM_container = $('<div class="DjangoCodeMirror"></div>');
        $(this).before(DCM_container);
        
        // Menu de boutons
        var header = $('<div class="DjangoCodeMirror_menu"><ul></ul><div class="cale"></div></div>');
        header.appendTo(DCM_container);
        // Déplace le textarea
        $(this).appendTo(DCM_container);
        // Onglets de preview
        if(settings.preview_url) {
            var footer = $('<div class="DjangoCodeMirror_tabs"><ul></ul><div class="cale"></div></div>');
            footer.appendTo(DCM_container);
            var tab_preview_on = $('<li class="tab preview"><a>Prévisualisation</a></li>');
            var tab_preview_off = $('<li class="tab editor tabactive"><a>Edition</a></li>');
            tab_preview_off.appendTo('.DjangoCodeMirror_tabs ul', DCM_container);
            tab_preview_on.appendTo('.DjangoCodeMirror_tabs ul', DCM_container);
            tab_preview_on.on("click", function(event){
                DCM_Core_Methods.previewRender(settings, DCM_container, codemirror_instance);
            });
            tab_preview_off.on("click", function(event){
                DCM_Core_Methods.closePreview(DCM_container, codemirror_instance);
            });
        }
        
        // Activation de CodeMirror
        codemirror_instance = CodeMirror.fromTextArea(this, settings);

        // Ajout des boutons pour le fullscreen si activé
        if( settings.fullscreen ){
            var maximize_settings = $.extend({}, default_button_settings, {
                name:'Maximiser',
                classname: 'buttonFullscreenEnter',
                functype:"fullscreenEnter"
            });
            var minimize_settings = $.extend({}, default_button_settings, {
                name:'Taille normale',
                classname: 'buttonFullscreenExit',
                functype:"fullscreenExit"
            });
            _add_bar_button(maximize_settings, DCM_container, codemirror_instance);
            _add_bar_button(minimize_settings, DCM_container, codemirror_instance);
            _add_bar_separator(DCM_container);
        }
        
        // Création des boutons des éléments de syntaxe
        $.each(DCM_Buttons_settings, function(item_index, item_value) {
            // options par défaut
            var item_settings = $.extend({}, default_button_settings, item_value);
            
            // Séparateur simple
            if(item_settings.separator) {
                _add_bar_separator(DCM_container);
            // Ajouter le bouton au DOM et créer son évènement de clic pour formatage
            } else {
                _add_bar_button(item_settings, DCM_container, codemirror_instance);
            }
        });
        
        // Ajout du lien de sauvegarde rapide
        if( settings.quicksave_url ){
            _add_bar_separator(DCM_container);
            var quicksave_settings = $.extend({}, default_button_settings, {
                name:'Sauvegarde rapide',
                classname: 'buttonQuickSave',
                quicksave_url: settings.quicksave_url,
                quicksave_datas: settings.quicksave_datas,
                csrf: settings.csrf,
                functype:"quicksave"
            });
            _add_bar_button(quicksave_settings, DCM_container, codemirror_instance);
        }
        
        // Ajout du lien d'aide si rempli
        if( settings.help_link ){
            _add_bar_separator(DCM_container);
            var help_settings = $.extend({}, default_button_settings, {
                name:'Aide',
                classname: 'buttonHelp',
                url: settings.help_link,
                functype:"externalressource"
            });
            _add_bar_button(help_settings, DCM_container, codemirror_instance);
        }
        
        $(window).bind('resize', function(event){
            resize(settings, DCM_container, codemirror_instance);
        });
        
        hlLine = codemirror_instance.setLineClass(0, "activeline");
        // Refresh de codemirror suite aux changements
        codemirror_instance.refresh();
    });
    
    /*
    * Add separator in buttons bar 
    */
    function _add_bar_separator(container) {
        $('<li class="separator">-----</li>').appendTo('.DjangoCodeMirror_menu ul', container);
    };
    
    /*
    * Add button to the bar
    */
    function _add_bar_button(item_opts, container, instance) {
        var accesskey = (item_opts.key) ? ' accesskey="'+item_opts.key+'"' : '';
        var button = $('<li class="button '+item_opts.classname+'"><a'+accesskey+' title="'+item_opts.name+'">'+item_opts.name+'</a></li>')
        button.appendTo('.DjangoCodeMirror_menu ul', container);
        button.on("click", item_opts, function(event){
            var opts = event.data;
            // Valeur de la séléction si elle n'est pas vide, sinon le @placeholder
            var value = instance.getSelection()||opts.placeholder;
            // Evaluation du nom de la méthode de formatage à employer
            if(opts.functype == 'fullscreenEnter' || opts.functype == 'fullscreenExit' || opts.functype == 'quicksave') {
                eval("DCM_Core_Methods."+opts.functype)(opts, container, instance);
            } else {
                eval("DCM_Syntax_Methods."+opts.functype)(value, instance, opts);
            }
            // Désactive la séléction pour replacer le curseur de X (0 par 
            // défaut) caractères après le texte qui était séléctionné
            var pos = instance.getCursor();
            pos.ch += 1;
            instance.setCursor(pos);
            // Rétablit le focus dans l'éditeur
            instance.focus();
        });
    };
    
    /*
    * Resize method to use for editor
    */
    function resize(djangocodemirror_settings, djangocodemirror_container, codemirror_instance) {
        // Redimensionnement du plein écran
        if ($("#DjangoCodeMirror_fullscreen_scene").length>0){
            var elems_css = DCM_Core_Methods.get_fullscreen_sizes(djangocodemirror_container, codemirror_instance);
            $("#DjangoCodeMirror_fullscreen_scene").css(elems_css[0]);
            $(".CodeMirror-scroll", djangocodemirror_container).css(elems_css[1]);
        }
        // Redimensionnement de la preview
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