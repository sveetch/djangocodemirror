/*
* Settings for DjangoCodeMirror buttons bar
*/
DCM_Buttons_settings = [
    {name:'Entête 1', classname: 'buttonH1', key:'1', char:'=', placeholder:'Titre', functype:"title" },
    {name:'Entête 2', classname: 'buttonH2', key:'2', char:'*', placeholder:'Titre', functype:"title" },
    {name:'Entête 3', classname: 'buttonH3', key:'3', char:'-', placeholder:'Titre', functype:"title" },
    {separator:true},
    {name:'Gras', classname: 'buttonBold', key:'B', placeholder:'totoz', begin_with:'**', close_with:'**', move_cursor_char:1 },
    {name:'Italique', classname: 'buttonItalic', key:'I', placeholder:'totoz', begin_with:'*', close_with:'*', move_cursor_char:1 },
    {name:'Code', classname: 'buttonCode', key:'T', placeholder:'totoz', begin_with:'``', close_with:'``', move_cursor_char:1 },
    {separator:true},
    {name:'Lien externe', classname: 'buttonLink', key:'A', placeholder:'totoz', functype:"link", move_cursor_char:1 },
    {name:'Lien vers une page interne', classname: 'buttonPageLink', key:'W', placeholder:'slug', begin_with:':page:`', close_with:'`', move_cursor_char:1 },
    {separator:true},
    {name:'Image par substitution', classname: 'buttonSubPicture', begin_with:'\n.. |', close_with:'| image:: lien image\n', placeholder:'nom_de_raccourci'},
    {name:'Image simple', classname: 'buttonPicture', begin_with:'.. image:: ', close_with:'\n', placeholder:'Votre lien d\'image'},
    {name:'Image annotée', classname: 'buttonFigure', begin_with:'.. figure:: ', close_with:'\n', placeholder:'Votre lien d\'image'},
    {separator:true},
    {name:'Liste à puces', classname: 'buttonBList', key:'L', functype:"bulletlist", placeholder:'Élément' },
    {name:'Liste numérotées', classname: 'buttonNList', functype:"numberedlist", placeholder:'Élément' },
    {separator:true},
    {name:'Citation', classname: 'buttonQuotes', begin_with:'    ', placeholder:'Citation', functype:"cite"},
    {name:'Code source coloré syntaxiquement', classname: 'buttonSourcecode', placeholder:'Votre code', functype:"sourcecode" }
];
