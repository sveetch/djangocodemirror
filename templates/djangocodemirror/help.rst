.. _CodeMirror: http://codemirror.net/
.. _Documentation de CodeMirror: http://codemirror.net/doc/manual.html
.. _jQuery: http://jquery.com/
.. _Django CSRF: https://docs.djangoproject.com/en/dev/ref/contrib/csrf/
.. _Django staticfiles: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/
.. _ReStructuredText: http://docutils.sourceforge.net/rst.html

Introduction
============

Cettre brique pour Django permet d'utiliser l'éditeur `CodeMirror`_ sur 
les *Textarea* avec un widget spécifique.

Prévu par défaut pour être utilisé par :page:`sveetchies-documents`, il utilise donc un environnement 
pour `ReStructuredText`_ et une interface supplémentaire à `CodeMirror`_. Cette interface qu'on appellera 
`DjangoCodeMirror`_ nécessite `jQuery`_ et ajouter quelques fonctionnalités supplémentaires :

* Une barre de boutons avec raccourcis clavier pour insérer des éléments de syntaxe;
* Possibilité de maximiser l'éditeur à la dimension complète de la fenêtre du navigateur;
* Un mode de prévisualisation compatible avec le système `Django CSRF`_;
* Un aspect visuel *renforcé* d'éditeur par rapport à `CodeMirror`_;

Par défaut, le plugin est prévu pour fonctionner avec le mode de syntaxe `ReStructuredText`_.

Requiert :

* `CodeMirror`_ (testé avec la version 2.21);
* `jQuery`_ >= 1.7;

Installation
============

Settings
********

Il suffit d'inscrire l'application à votre projet, en modifiant ``INSTALLED_APPS`` dans vos ``settings`` 
en y rajoutant ces deux lignes :

..  sourcecode:: python
    :linenos:
    :hl_lines: 3

    INSTALLED_APPS = (
        ...
        'Sveetchies.django.djangocodemirror',
        ...
    )

Il est aussi nécessaire que vous installiez une copie de **CodeMirror** dans vos *statics*, l'emplacement par 
défaut prévu est dans un répertoire ``CodeMirror/`` à la racine de vos *statics*. Vous devez aussi posséder 
une copie de jQuery et le déclarer vous mêmes dans vos *templates*.

Utilisation
===========

DjangoCodeMirror
****************

L'éditeur `DjangoCodeMirror`_ est une *surcouche* de `CodeMirror`_ construit comme un plugin `jQuery`_. Lors de son instanciation le 
plugin accepte les mêmes paramètres que `CodeMirror`_ avec quelques options supplémentaires :

* ``preview_url``: Attends une chaîne de caractères, si rempli le mode de prévisualisation est utilisé et l'URL 
  donnée sera utilisée pour envoyer une requête POST qui attends une réponse HTML avec le fragment HTML du rendu 
  de prévisualisation;
* ``csrf``: Attends une chaine de caractères représentant le nom de la fonction à utiliser lors de la prévisualisation 
  pour insérer un *header* décrivant le *token* `Django CSRF`_;
* ``preview_padding`` : Taille (en pixels) du padding de l'éditeur en mode prévisualisation. Il est déconseillé d'y toucher et 
  il sera probablement *deprecated* d'içi peu;
* ``preview_borders``: Épaisseur (en pixels) de la bordure du cadre de l'éditeur en mode prévisualisation. Il est déconseillé 
  d'y toucher et il sera probablement *deprecated* d'içi peu.

``DjangoCodeMirror`` est **l'éditeur par défaut**, mais il est possible d'utiliser uniquement `CodeMirror`_ sans le plugin 
`jQuery`_, dans ce cas là les options cités ci-dessus n'ont aucun intérêt.

CodeMirrorWidget
****************

Vous pouvez déclarer le widget ``Sveetchies.django.djangocodemirror.fields.CodeMirrorWidget`` sur vos champs de 
formulaires :

..  sourcecode:: python
    :linenos:
    :hl_lines: 4

    from Sveetchies.django.djangocodemirror.fields import CodeMirrorWidget
    
    class CodeMirrorSampleForm(forms.Form):
        content = forms.CharField(label=u"Votre texte", widget=CodeMirrorWidget)
        
        def save(self, *args, **kwargs):
            return

En plus de l'attribut ``attrs`` habituel des widgets, `CodeMirrorWidget`_ accepte aussi deux arguments 
optionnels supplémentaires :

* ``codemirror_only`` désactive l'utilisation de `DjangoCodeMirror`_ et utilise à la place `CodeMirror`_;
* ``codemirror_attrs`` : attends un dictionnaire des paramètres d'instanciation de l'éditeur.

Par exemple :

..  sourcecode:: python
    :linenos:
    :hl_lines: 4

    from Sveetchies.django.djangocodemirror.fields import CodeMirrorWidget
    
    class CodeMirrorSampleForm(forms.Form):
        content = forms.CharField(label=u"Votre texte", widget=CodeMirrorWidget(codemirror_only=True, codemirror_attrs={'lineNumbers':True}))
        
        def save(self, *args, **kwargs):
            return

Avec ceci le champ ``content`` utilisera l'éditeur `CodeMirror`_ en activant la numérotation des lignes.

Médias
------

Dans votre template, il faudra charger les médias liés au formulaire (et donc au widget) en utilisant par 
exemple : ::

  {{ form.media }}

CodeMirrorField
***************

Ce champ de formulaire est un héritage de ``django.forms.CharField`` qui intègre directement le widget 
`CodeMirrorWidget`_ en y forcant l'option ``codemirror_only`` pour n'utiliser que l'éditeur `CodeMirror`_.

En outre des arguments de ``django.forms.CharField`` il accepte aussi l'argument optionnel 
``codemirror_attrs`` de la même manière qu'avec `CodeMirrorWidget`_.

..  sourcecode:: python
    :linenos:
    :hl_lines: 5

    from django import forms
    from Sveetchies.django.djangocodemirror.fields import CodeMirrorField
    
    class CodeMirrorSampleForm(forms.Form):
        content_codemirror = CodeMirrorField(label=u"Votre texte", codemirror_attrs={'lineNumbers':True})
        
        def save(self, *args, **kwargs):
            return

DjangoCodeMirrorField
*********************

De la même manière que `CodeMirrorField`_, ce champ est un héritage de ``django.forms.CharField`` qui intègre 
directement le widget `CodeMirrorWidget`_ mais pour utiliser l'éditeur `DjangoCodeMirror`_.

Il se comporte de la même façon que `CodeMirrorField`_ et accepte le même argument optionnel ``codemirror_attrs``.

..  sourcecode:: python
    :linenos:
    :hl_lines: 5

    from django import forms
    from Sveetchies.django.djangocodemirror.fields import CodeMirrorField
    
    class CodeMirrorSampleForm(forms.Form):
        content_djangocodemirror = DjangoCodeMirrorField(label=u"Votre texte", codemirror_attrs={'lineNumbers':True})
        
        def save(self, *args, **kwargs):
            return

Options
=======

Il est possible de contrôler certains comportements de l'éditeur depuis vos *settings* via les variables suivantes. 
Vous pouvez retrouver toute les valeurs par défaut de ces variables sont dans ``Sveetchies.django.djangocodemirror``.

DJANGOCODEMIRROR_FIELD_INIT_JS
******************************

Le code HTML d'instanciation de `DjangoCodeMirror`_ sur un champ de formulaire. C'est un *template* de chaîne
de caractère utilisable avec ``String.format()`` qui recevra deux variables :

* *inputid* : l'identifiant unique du champ sur lequel instancier l'éditeur;
* *settings* : une chaîne de caractères contenant les options d'instanciations de l'éditeur au format JSON.

CODEMIRROR_FIELD_INIT_JS
************************

Le code HTML d'instanciation de `CodeMirror`_ sur un champ de formulaire. C'est un *template* de chaîne

CODEMIRROR_SETTINGS
*******************

Un dictionnaire contenant différents schémas d'options pour les éditeurs. Vous pouvez y mettre toute les 
options attendues par `CodeMirror`_ plus celles de `DjangoCodeMirror`_. À noter que dans les templates ces options 
sont transmises aux éditeurs dans un format JSON.

Par défaut quelques schémas d'options sont fournis :

* ``default`` : Ne fait que définir l'option pour activer la numérotation des lignes;
* ``djangocodemirror`` : Définit les options minimales pour `DjangoCodeMirror`_ (numérotation des lignes et le mode 
  de syntaxe ``rst`` pour `ReStructuredText`_);
* ``djangocodemirror_with_preview`` : Reprends les mêmes options que ``djangocodemirror`` plus celle pour activer la 
  prévisualisation sur l'URL ``/preview/``.

DJANGOCODEMIRROR_DEFAULT_SETTING
********************************

Le nom clé du schéma par défaut à utiliser pour `DjangoCodeMirror`_ tel qu'avec le champ `DjangoCodeMirrorField`_.

CODEMIRROR_MODES
****************

Une liste de *tuple* des différents modes de syntaxe disponibles pour `CodeMirror`_. La liste contenue par défaut 
est une liste reproduite à partir de tout les modules officiels existants `CodeMirror`_.

Chemins relatifs des médias
***************************

Vous pouvez si besoin, modifier tout les chemins des médias liés au widget `CodeMirrorWidget`_. Leur chemin est 
relatif à votre emplacement des fichiers statiques (voyez `Django staticfiles`_) ou des médias si vous n'utilisez 
pas les *staticfiles*.

Ci-dessous les différents chemins :

* ``CODEMIRROR_FILEPATH_LIB`` : La librairie JavaScript de `CodeMirror`_;
* ``CODEMIRROR_FILEPATH_CSS`` : Le fichier CSS de `CodeMirror`_;
* ``DJANGOCODEMIRROR_FILEPATH_LIB`` : La librairie JavaScript de `DjangoCodeMirror`_;
* ``DJANGOCODEMIRROR_FILEPATH_CSS`` : Le fichier CSS de `DjangoCodeMirror`_;
* ``DJANGOCODEMIRROR_FILEPATH_CSRF`` : Le composant JavaScript de permettant le support du système `Django CSRF`_ 
  dans les prévisualisations avec `DjangoCodeMirror`_;
* ``DJANGOCODEMIRROR_FILEPATH_COOKIES`` : Le plugin `jQuery`_ pour utiliser accéder aux cookies, nécessaire 
  pour `Django CSRF`_;

Par défaut, tout ces chemins sont configurés pour fonctionner avec les médias déjà fournis dans la brique logicielle. 
Vous pouvez les modifier selon vos besoins.