# -*- coding: utf-8 -*-
import sys
sys.path[0:0] = [
  '/home/django/Emencia/parrot-oem/eggs/Pillow-1.7.8-py2.6-linux-x86_64.egg',
  '/home/django/Emencia/parrot-oem/eggs/Django-1.4.6-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_cms-2.3.7-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_filebrowser_no_grappelli-3.1.1-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/sorl_thumbnail-11.12-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/djangocms_text_ckeditor-1.0.10-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/South-0.7.6-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/crispy_forms_foundation-0.2.2-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_blog_zinnia-0.12.3-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/cmsplugin_zinnia-0.4-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_admin_tools-0.5.1-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_assets-0.8-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/yuicompressor-2.4.7-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/argparse-1.2.1-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_debug_toolbar-0.9.4-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_google_tools-1.0.0-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_excel_response-1.0-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_recaptcha-0.0.6-py2.6.egg',
  '/home/django/Emencia/parrot-oem/django-apps-src/djangocodemirror',
  '/home/django/Emencia/parrot-oem/eggs/emencia.django.countries-0.1-py2.6.egg',
  '/home/django/Emencia/parrot-oem/django-apps-src/emencia-cms-snippet',
  '/home/django/Emencia/parrot-oem/django-apps-src/emencia-django-slideshows',
  '/home/django/Emencia/parrot-oem/eggs/django_registration-1.0-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/djangorecipe-1.5-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/zc.recipe.egg-2.0.0-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/zc.buildout-2.2.0-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/setuptools-0.8-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/rstview-0.2-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/webassets-0.8-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/pytz-2013b-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/pyparsing-1.5.7-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_xmlrpc-0.1.5-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_tagging-0.3.1-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_mptt-0.5.2-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/BeautifulSoup-3.2.1-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_crispy_forms-1.2.7-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/html5lib-0.95-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_sekizai-0.7-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/django_classy_tags-0.4-py2.6.egg',
  '/home/django/Emencia/parrot-oem/eggs/docutils-0.11-py2.6.egg',
  '/home/django/Emencia/parrot-oem',
]

import os
os.environ['DJANGO_SETTINGS_MODULE'] = "project.settings_development"

#from django.test import TestCase
import unittest

from django.core.urlresolvers import reverse
from djangocodemirror import settings_local
from djangocodemirror.config import ConfigManager

#class ConfigTest(TestCase):
class ConfigTest(unittest.TestCase):
    """Test the config object"""
    
    def test_01_empty(self):
        """Just checkin with an empty init"""
        ConfigManager()
    
    def test_02_kwargs_init(self):
        """Checking only init with kwargs"""
        config = ConfigManager(
            codemirror_only=False,
            embed_settings=True,
            add_jquery=True,
        )
        self.assertFalse('codemirror_attrs' in config.settings)
        self.assertFalse(config.settings['codemirror_only'])
        self.assertTrue(config.settings['embed_settings'])
        self.assertTrue(config.settings['add_jquery'])
    
    def test_03_config_init(self):
        """Checking init with given config dict"""
        config = ConfigManager(codemirror_attrs={
            'codemirror_only': True,
            'embed_settings': True,
            'add_jquery': True,
        })
        self.assertFalse('codemirror_attrs' in config.settings)
        self.assertTrue(config.settings['codemirror_only'])
        self.assertTrue(config.settings['embed_settings'])
        self.assertEqual(config.settings['add_jquery'], settings_local.DEFAULT_JQUERY_PATH)
    
    def test_04_config_n_kwargs_init(self):
        """Checking init with kwargs and given config dict"""
        config = ConfigManager(
            codemirror_attrs={
                'codemirror_only': True,
                'embed_settings': False,
                'add_jquery': True,
            },
            codemirror_only=False,
            embed_settings=True,
            add_jquery=True
        )
        self.assertFalse(config.settings['codemirror_only'])
        self.assertTrue(config.settings['embed_settings'])
        self.assertEqual(config.settings['add_jquery'], settings_local.DEFAULT_JQUERY_PATH)
    
    def test_05_opt_current_mode(self):
        """Checking option mode"""
        # empty
        config1 = ConfigManager(
            codemirror_attrs={
                'mode': None
            },
        )
        self.assertEqual(config1.settings['current_mode_name'], None)
        self.assertEqual(config1.settings['current_mode_path'], None)
        # simple value resolving
        config2 = ConfigManager(
            codemirror_attrs={
                'mode': 'rst'
            },
        )
        self.assertEqual(config2.settings['current_mode_name'], 'rst')
        self.assertEqual(config2.settings['current_mode_path'], dict(settings_local.CODEMIRROR_MODES).get('rst', None))
        # dict value resolving
        config3 = ConfigManager(
            codemirror_attrs={
                'mode': {'name': "jinja2", 'htmlMode': True}
            },
        )
        self.assertEqual(config3.settings['current_mode_name'], 'jinja2')
        self.assertEqual(config3.settings['current_mode_path'], dict(settings_local.CODEMIRROR_MODES).get('jinja2', None))
        # merge isntance kwargs with given config
        config4 = ConfigManager(
            codemirror_attrs={
                'mode': 'rst'
            },
            mode={'name': "python", 'htmlMode': False}
        )
        self.assertEqual(config4.settings['current_mode_name'], 'python')
        self.assertEqual(config4.settings['current_mode_path'], dict(settings_local.CODEMIRROR_MODES).get('python', None))
    
    def test_06_opt_add_jquery(self):
        """Checking option add_jquery"""
        # Empty
        config1 = ConfigManager(codemirror_attrs={
            'add_jquery': False,
        })
        self.assertFalse(config1.settings['add_jquery'])
        # Default value in given config
        config2 = ConfigManager(codemirror_attrs={
            'add_jquery': True,
        })
        self.assertEqual(config2.settings['add_jquery'], settings_local.DEFAULT_JQUERY_PATH)
        # Custom value than overwrites the one in config
        config3 = ConfigManager(
            codemirror_attrs={
                'add_jquery': True,
            },
            add_jquery="foo/bar.js"
        )
        self.assertEqual(config3.settings['add_jquery'], "foo/bar.js")
    
    def test_07_publish_config(self):
        """Checking editor_config attribute output"""
        # Empty
        config = ConfigManager(
            codemirror_attrs={
                'codemirror_only': True,
                'embed_settings': False,
                'add_jquery': True,
                'mode': 'rst',
                'lineWrapping': False,
                'lineNumbers': True,
            },
            codemirror_only=False,
            embed_settings=True,
            add_jquery=True,
            mode={'name': "python", 'htmlMode': False}
        )
        self.assertEqual(config.editor_config, {
            'mode': {'name': "python", 'htmlMode': False},
            'lineWrapping': False,
            'lineNumbers': True,
        })
    
    def test_08_reverse_urls(self):
        """Checking urls reversing in config"""
        config = ConfigManager(
            codemirror_attrs={
                'mode': 'rst',
                'preview_url': ('djangocodemirror-sample-preview', [], {}),
                'quicksave_url': ('djangocodemirror-sample-quicksave', [], {}),
                'settings_url': ('djangocodemirror-settings', [], {}),
            },
        )
        self.assertEqual(config.editor_config, {
            'mode': 'rst',
            'preview_url': reverse('djangocodemirror-sample-preview'),
            'quicksave_url': reverse('djangocodemirror-sample-quicksave'),
            'settings_url': reverse('djangocodemirror-settings'),
        })
    
    def test_09_merge_config(self):
        """Checking config merge"""
        # Init with various options
        config = ConfigManager(
            codemirror_attrs={
                'codemirror_only': True,
                'embed_settings': False,
                'add_jquery': True,
                'mode': 'rst',
                'lineWrapping': False,
                'lineNumbers': True,
                'preview_url': "/foo/bar/",
            },
            codemirror_only=False,
            embed_settings=True,
            add_jquery=True,
            mode={'name': "python", 'htmlMode': False}
        )
        self.assertEqual(config.editor_config, {
            'mode': {'name': "python", 'htmlMode': False},
            'lineWrapping': False,
            'lineNumbers': True,
            'preview_url': "/foo/bar/",
        })
        
        # Push new options to merge
        config.merge_config(**{
            'codemirror_only': True,
            'embed_settings': True,
            'mode': 'jinja2',
            'add_jquery': "/foo/bar.js",
            'lineWrapping': True,
            'preview_url': ('djangocodemirror-sample-preview', [], {}),
            'quicksave_url': ('djangocodemirror-sample-quicksave', [], {}),
        })
        self.assertEqual(config.editor_config, {
            'mode': 'jinja2',
            'lineWrapping': True,
            'lineNumbers': True,
            'preview_url': reverse('djangocodemirror-sample-preview'),
            'quicksave_url': reverse('djangocodemirror-sample-quicksave'),
        })
        self.assertTrue(config.settings['codemirror_only'])
        self.assertTrue(config.settings['embed_settings'])
        self.assertEqual(config.settings['add_jquery'], "/foo/bar.js")
    
    def test_10_setting_name(self):
        """Test to resolve settings from the setting name"""
        config = ConfigManager(
            codemirror_settings_name='djangocodemirror_with_preview'
        )
        self.assertEqual(config.settings['codemirror_settings_name'], "djangocodemirror_with_preview")
        self.assertEqual(config.settings['mode'], "rst")
        self.assertTrue(config.settings['lineNumbers'])

if __name__ == '__main__':
    unittest.main()