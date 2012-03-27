.. _CodeMirror: http://codemirror.net/
.. _Documentation de CodeMirror: http://codemirror.net/doc/manual.html
.. _jQuery: http://jquery.com/
.. _jQuery.axax(): http://api.jquery.com/jQuery.ajax/
.. _Django CSRF: https://docs.djangoproject.com/en/dev/ref/contrib/csrf/
.. _Django staticfiles: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/
.. _ReStructuredText: http://docutils.sourceforge.net/rst.html
.. _qTip2: http://craigsworks.com/projects/qtip2/

Introduction
============

.. WARNING:: This is a temporary commit, README should be translated and references to 
             **Sveetchies-documents** should be move to his future export in Github.

Cette brique pour Django permet d'utiliser l'éditeur `CodeMirror`_ sur 
les *Textarea* avec un widget spécifique.

Prévu par défaut pour être utilisé par **sveetchies-documents**, il utilise donc un environnement 
pour `ReStructuredText`_ et une interface supplémentaire à `CodeMirror`_. Cette interface qu'on appellera 
`DjangoCodeMirror`_ nécessite `jQuery`_, elle ajoute quelques fonctionnalités supplémentaires :

* Une barre de boutons avec raccourcis clavier pour insérer des éléments de syntaxe;
* Possibilité de maximiser l'éditeur à la dimension complète de la fenêtre du navigateur;
* Un mode de prévisualisation compatible avec le système `Django CSRF`_;
* Un aspect visuel *renforcé* d'éditeur par rapport à `CodeMirror`_;

Par défaut, le plugin est prévu pour fonctionner avec le mode de syntaxe `ReStructuredText`_ que vous pouvez 
remplacer par un autre des modes de syntaxe de `CodeMirror`_ ou un des votres.

Requiert :

* `jQuery`_ >= 1.7;

Installation
============

Settings
********

Il suffit d'inscrire l'application à votre projet, en modifiant ``INSTALLED_APPS`` dans vos ``settings`` 
en y rajoutant ces deux lignes : ::

    INSTALLED_APPS = (
        ...
        'djangocodemirror',
        ...
    )

Il est aussi nécessaire que vous installiez une copie de `CodeMirror`_ dans vos *statics* `Django staticfiles`_, 
l'emplacement par défaut prévu est dans un répertoire ``CodeMirror/`` à la racine de vos *statics*. Vous devez 
aussi posséder une copie de `jQuery`_ et le déclarer vous mêmes dans vos *templates*.

Utilisation
===========

DjangoCodeMirror
****************

L'éditeur `DjangoCodeMirror`_ est une *surcouche* de `CodeMirror`_ et construit comme un plugin `jQuery`_. Lors 
de son instanciation le plugin accepte les mêmes paramètres que `CodeMirror`_ avec quelques options 
supplémentaires :

fullscreen
  Active le mode pour maximiser l'éditeur si ``true``, désactivé si ``false``. Il est activé par défaut.
help_link
  Lien à utiliser pour la page d'aide si rempli (par une chaîne de caractères), sinon le bouton d'aide n'est pas 
  affiché. À noter que le lien est toujours ouvert dans une nouvelle fenêtre.
quicksave_url
  URL où envoyer les données à travers une requête de type **POST** en utilisant l'option de ``csrf`` 
  si il est activé. Vide et donc désactivé par défaut. 
  
  La requête envoi les variables suivantes :
  
  * ``nocache`` : un *timestamp* qui sert uniquement à empêche la mise en cache des requêtes par certains vieux 
    navigateurs;
  * ``content`` : le contenu du *Textarea* tel qu'il est au moment de l'envoi de la requête.
quicksave_datas
  Objet (``{..}``) de variables à transmettre dans la requête de sauvegarde rapide. Peut être 
  aussi une chaîne de caractères qui sera considérée comme un nom de variable à utiliser pour retrouver l'objet à 
  transmettre, c'est la technique à préférer dans le cas d'utilisation de `DjangoCodeMirrorField`_ et `CodeMirrorWidget`_ 
  pour éviter d'avoir à transmettre l'instance du contenu dans les options lors de l'instanciation du formulaire.
preview_url
  Attends une chaîne de caractères, si rempli le mode de prévisualisation est utilisé et l'URL 
  donnée sera utilisée pour envoyer une requête **POST** qui attends une réponse HTML avec le fragment HTML du rendu 
  de prévisualisation. Utilise l'option de ``csrf`` si il est activé.
  
  La requête envoi les variables suivantes :
  
  * ``nocache`` : un *timestamp* qui sert uniquement à empêche la mise en cache des requêtes par certains vieux 
    navigateurs;
  * ``content`` : le contenu du *Textarea* tel qu'il est au moment de l'envoi de la requête.
csrf
  Attends une chaine de caractères représentant le nom de la fonction à utiliser lors de la prévisualisation 
  pour insérer un *header* décrivant le *token* de `Django CSRF`_. Désactivé par défaut.
  
  La fonction attends deux arguments obligatoires :
  
  * xhr : une fonction de *callback* de la requête produite par `jQuery`_ qui permet de la modifier avant son envoi;
  * settings : objet des options passées à `jQuery.axax()`_.
  
  Cette fonction est destinée à une utilisation dans l'option ``beforeSend`` de `jQuery.axax()`_ pour récupérer le *token csrf* 
  dans les cookies et le transmettre dans la requête.
preview_padding
  Taille (en pixels) du padding de l'éditeur en mode prévisualisation. Il est déconseillé d'y toucher et 
  il sera probablement *deprecated* d'içi peu.
preview_borders
  Épaisseur (en pixels) de la bordure du cadre de l'éditeur en mode prévisualisation. Il est déconseillé 
  d'y toucher et il sera probablement *deprecated* d'içi peu.

Ces options n'ont d'intérêt que dans le contexte de `DjangoCodeMirror`_ et `CodeMirror`_ n'en a aucune utilité.

Un exemple complet d'instanciation directe : ::

    <div>
        <textarea id="id_content" rows="10" cols="40" name="content"></textarea>
        <script language="JavaScript" type="text/javascript">
        //<![CDATA[
            $(document).ready(function() {
                id_content_codemirror_instance = $('#id_content').djangocodemirror({
                    "mode": "rst",
                    "csrf": "CSRFpass",
                    "quicksave_url": "/djangocodemirror-sample/quicksave/",
                    "preview_url": "/djangocodemirror-sample/preview/",
                    "lineWrapping": true,
                    "lineNumbers": true
                });
            });
        //]]>
        </script>
    </div>

`DjangoCodeMirror`_ embarque :

* Une copie de `CodeMirror`_;
* Une fonction de **csrf** pour utiliser la technique de `Django CSRF`_;
* Une copie du plugin `jquery.cookies <http://plugins.jquery.com/project/Cookie>`_ utilisé uniquement par la fonction de **csrf**;
* Une copie du plugin `qTip2`_;

CodeMirrorWidget
****************

Vous pouvez déclarer le widget ``djangocodemirror.fields.CodeMirrorWidget`` sur un champ de 
formulaire de la façon suivante : ::

    from djangocodemirror.fields import CodeMirrorWidget
    
    class CodeMirrorSampleForm(forms.Form):
        content = forms.CharField(label=u"Votre texte", widget=CodeMirrorWidget)
        
        def save(self, *args, **kwargs):
            return

En plus de l'attribut ``attrs`` habituel d'un widget, `CodeMirrorWidget`_ accepte aussi deux arguments 
optionnels supplémentaires :

* ``codemirror_only`` désactive l'utilisation de `DjangoCodeMirror`_ et utilise à la place `CodeMirror`_;
* ``codemirror_attrs`` : attends un dictionnaire des paramètres d'instanciation de l'éditeur.

Par exemple : ::

    from djangocodemirror.fields import CodeMirrorWidget
    
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

::

    from django import forms
    from djangocodemirror.fields import CodeMirrorField
    
    class CodeMirrorSampleForm(forms.Form):
        content_codemirror = CodeMirrorField(label=u"Votre texte", codemirror_attrs={'lineNumbers':True})
        
        def save(self, *args, **kwargs):
            return

DjangoCodeMirrorField
*********************

De la même manière que `CodeMirrorField`_, ce champ est un héritage de ``django.forms.CharField`` qui intègre 
directement le widget `CodeMirrorWidget`_ mais pour utiliser l'éditeur `DjangoCodeMirror`_.

Il se comporte de la même façon que `CodeMirrorField`_ et accepte le même argument optionnel ``codemirror_attrs``.

::

    from django import forms
    from djangocodemirror.fields import CodeMirrorField
    
    class CodeMirrorSampleForm(forms.Form):
        content_djangocodemirror = DjangoCodeMirrorField(label=u"Votre texte", codemirror_attrs={'lineNumbers':True})
        
        def save(self, *args, **kwargs):
            return

Options
=======

Il est possible de contrôler certains comportements de l'éditeur depuis vos *settings* via les variables suivantes. 
Vous pourrez retrouver toute les valeurs par défaut de ces variables dans ``djangocodemirror``.

DJANGOCODEMIRROR_FIELD_INIT_JS
******************************

Le code HTML d'instanciation de `DjangoCodeMirror`_ sur un champ de formulaire. C'est un *template* de chaîne
de caractère utilisable avec ``String.format()`` qui recevra deux variables :

* ``inputid`` : l'identifiant unique du champ sur lequel instancier l'éditeur;
* ``settings`` : une chaîne de caractères contenant les options d'instanciations de l'éditeur au format JSON.

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
* ``djangocodemirror_sample_demo`` : Reprends les mêmes options que ``djangocodemirror_with_preview`` mais calibrés 
  pour fonctionner dans le cadre de `Ensemble de démonstration`_.

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

CODEMIRROR_FILEPATH_LIB
  La librairie JavaScript de `CodeMirror`_.
CODEMIRROR_FILEPATH_CSS
  Le fichier CSS de `CodeMirror`_.
DJANGOCODEMIRROR_FILEPATH_LIB
  La librairie JavaScript de `DjangoCodeMirror`_.
DJANGOCODEMIRROR_FILEPATH_CSS
  Le fichier CSS de `DjangoCodeMirror`_.
DJANGOCODEMIRROR_FILEPATH_BUTTONS
  Composant JavaScript définissant les boutons disponibles dans l'éditeur, à surclasser (en crééant le votre et 
  renseignant son chemin à la place dans vos **settings**).
DJANGOCODEMIRROR_FILEPATH_METHODS
  Composant JavaScript définissant les méthodes utilisés par les boutons disponibles de l'éditeur, à surclasser 
  (en crééant le votre et renseignant son chemin à la place dans vos **settings**).
DJANGOCODEMIRROR_FILEPATH_CONSOLE
  Composant JavaScript pour les notifications de l'éditeur.
DJANGOCODEMIRROR_FILEPATH_CSRF
  Le composant JavaScript de permettant le support du système `Django CSRF`_ dans les prévisualisations avec `DjangoCodeMirror`_.
DJANGOCODEMIRROR_FILEPATH_COOKIES
  Le plugin `jQuery`_ pour utiliser accéder aux cookies, nécessaire pour `Django CSRF`_.
QTIP_FILEPATH_LIB
  La librairie JavaScript de `qTip2`_.
QTIP_FILEPATH_CSS
  Le fichier CSS de `qTip2`_.

Par défaut tout ces chemins sont déjà configurés pour fonctionner avec les médias déjà fournis dans la brique 
logicielle mais vous pouvez les modifier selon vos besoins.

Ensemble de démonstration
=========================

Un ensemble de démonstration complet est inclus dans ``djangocodemirror.views`` et dans 
``djangocodemirror.urls``.

Vous pouvez l'inclure à votre projet simplement en incluant ses urls à votre fichier ``urls.py`` de votre 
projet : ::

    urlpatterns = patterns('',
        ...
        (r'^djangocodemirror-sample/', include('djangocodemirror.urls')),
        ...
    )

Trois vues y sont présentes :

* L'index (donc ``djangocodemirror-sample/`` si vous n'avez pas changé le point de montage des urls) qui affiche 
  la démonstration utilisant le mode de syntaxe pour `ReStructuredText`_;
* ``preview/`` pour la prévisualisation de l'éditeur, utilise le parser de **sveetchies-documents** si il est 
  disponible, sinon renvoi un contenu *bidon*. N'accepte que les requêtes de type **POST**, renverra une simple 
  réponse vide pour toute requête de type **GET**;
* ``quicksave/`` pour simuler la sauvegarde rapide. N'effectue aucune sauvegarde mais test au moins le contenu pour 
  renvoyer une erreur le cas échéant. La validation utilise le parser **sveetchies-documents** si il est installé 
  sinon aucune réelle validation de syntaxe n'est effectuée (seulement celle du formulaire);
