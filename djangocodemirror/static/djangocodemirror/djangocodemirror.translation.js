/*
* Translations methods and registry for DjangoCodeMirror
*/
DCM_lang = "en";
DCM_Translations = {};

/*
* Get the translation from the given key and finded language
* 
* If lang is not given, use the default language. Keys should be strings writed in the 
* default language so he don't need to have a translation.
* 
* If the key or lang does not exist in the registry, this simply return the given 
* key.
*/
function safegettext(key, lang) {
    if (!lang) {
        lang = DCM_lang;
    }
    if(DCM_Translations[lang]) {
        if(DCM_Translations[lang][key]) {
            return DCM_Translations[lang][key];
        }
    }
    return key;
};
