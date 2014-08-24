# -*- coding: utf-8 -*-
"""
DjangoCodeMirror config object
"""
import copy, json

from django.core.urlresolvers import reverse

from djangocodemirror import settings_local

class ConfigManager(object):
    """
    Editor object to store config and publish clean asset list and javascript settings
    
    * 'Real' config options are the instance attributes;
    * 'codemirror_attrs' is only used to pass config as a dict, some these option can be overriden by given class arguments
    * public config is a dict returned without items from '_default_app_settings'
    """
    # Only internal settings, no public javascript settings
    _default_app_settings = {
        'codemirror_only': None,
        'embed_settings': None,
        'csrf': None,
        'search_enabled': None,
        
        'mode': None,
        'current_mode_name': None,
        'current_mode_path': None,
        
        'themes': [item[1] for item in settings_local.CODEMIRROR_THEMES],
        'translations': settings_local.DJANGOCODEMIRROR_TRANSLATIONS,
        
        'codemirror_settings_name': 'default',
        'css_bundle_name': settings_local.BUNDLES_CSS_NAME.format(settings_name='default'),
        'js_bundle_name': settings_local.BUNDLES_JS_NAME.format(settings_name='default'),
        'lib_buttons_path': settings_local.DJANGOCODEMIRROR_LIB_BUTTONS_PATH,
        'lib_syntax_methods_path': settings_local.DJANGOCODEMIRROR_LIB_SYNTAX_METHODS_PATH,
    }
    # Various keys that settings can receive, especially the ones from widgets attrs (cols, rows, etc..)
    _filtred = ['id', 'name', 'rows', 'cols']
    # Internal settings authorized to be passed to public conf
    _pass_to_public = {
        #INTERNAL_NAME: PUBLIC_NAME,
        'mode': None,
        'csrf': None,
    }
    
    def __init__(self, config_name='default'):
        self.config_name = config_name
        self.settings = copy.deepcopy(self._default_app_settings)
        self.settings.update(copy.deepcopy(settings_local.CODEMIRROR_SETTINGS[config_name]))
        
        
        self.settings['css_bundle_name'] = settings_local.BUNDLES_CSS_NAME.format(settings_name=config_name)
        self.settings['js_bundle_name'] = settings_local.BUNDLES_JS_NAME.format(settings_name=config_name)
        
        if 'mode' in self.settings and self.settings['mode']:
            self.settings['current_mode_name'], self.settings['current_mode_path'] = self._resolve_mode(self.settings['mode'])
    
    def debug_internal_config(self):
        print "="*60
        print "INTERNAL CONFIG"
        print "="*60
        print 
        print json.dumps(self.settings, indent=4)
    
    def debug_editor_config(self):
        print "="*60
        print "EDITOR CONFIG"
        print "="*60
        print 
        print json.dumps(self.editor_config, indent=4)
    
    def _publish_editor_config(self):
        """
        Return a dict config only with public options (with reversed urls if any)
        """
        published = copy.deepcopy(self.settings)
        filtred = [a for a in self._default_app_settings.keys() if a not in self._pass_to_public]
        # Remove internal values except those from authorized list '_pass_to_public'
        for opt in self.settings:
            if opt in filtred:
                del published[opt]
        # Rename keys from '_pass_to_public'
        for original,changed in self._pass_to_public.items():
            # Only if changed is not empty and different from original
            if original in published and changed and changed != original:
                published[changed] = published[original]
                del published[original]
        
        return self._reverse_setting_urls(published)
    editor_config = property(_publish_editor_config)
    
    def _resolve_mode(self, mode):
        """
        Return the right app config (a dict)
        """
        name = mode
        if isinstance(name, dict):
            name = mode['name']
        path = dict(settings_local.CODEMIRROR_MODES).get(name, None)
        
        return name, path

    def _reverse_setting_urls(self, app_config):
        """
        Reverse url items that are tuple ``(urlname, args, kwargs)``.
        
        Limited to items : preview_url, help_link, quicksave_url, settings_url
        """
        for name in ['preview_url', 'help_link', 'quicksave_url', 'settings_url']:
            if name in app_config and app_config.get(name, None) is not None and not isinstance(app_config.get(name, None), basestring):
                args = []
                kwargs = {}
                urlname = app_config[name][0]
                if len(app_config[name])>1:
                    args = app_config[name][1]
                    if len(app_config[name])>2:
                        kwargs = app_config[name][2]
                app_config[name] = reverse(urlname, args=args, kwargs=kwargs)
        return app_config
    
    def find_assets(self):
        """
        Return the right app settings (a dict) for the given widget instance
        """
        css, js = [], []
        
        js.append("CodeMirror/lib/codemirror.js")
        
        if self.settings['search_enabled']:
            js.append("CodeMirror/lib/util/dialog.js")
            js.append("CodeMirror/lib/util/search.js")
            js.append("CodeMirror/lib/util/searchcursor.js")
        
        if self.settings['current_mode_path']:
            js.append(self.settings['current_mode_path'])
        
        if self.settings['codemirror_only']:
            css.append("CodeMirror/lib/codemirror.css")
        else:
            css.append("css/djangocodemirror.css")
            
            #js.append("js/jquery/jquery.cookies.2.2.0.js")
            js.append("djangocodemirror/djangocodemirror.translation.js")
            
            for item in self.settings['translations']:
                js.append(item)

            js.append(self.settings['lib_buttons_path'])
            js.append(self.settings['lib_syntax_methods_path'])
            js.append("djangocodemirror/djangocodemirror.js")

            if self.settings['csrf']:
                js.append("djangocodemirror/csrf.js")
        
        for item in self.settings['themes']:
            css.append(item)
        
        return css, js
