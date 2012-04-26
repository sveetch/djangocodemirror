/*
// CSRF method for token transition within Ajax requests. The Token is extraced from 
// the Django cookie "csrftoken".
//
// Cf: https://docs.djangoproject.com/en/dev/ref/contrib/csrf/
//
// Require:
//
// * jQuery >= 1.5.1
// * jQuery plugin for cookies that enable a "$.cookie"
//
// Direct usage in your ajax process :
//
//     $.ajax({
//         type: "POST",
//         dataType: "json",
//         beforeSend: CSRFpass,
//         url: "/foo/",
//     });
//
// Apply to all ajax process in your page :
//
//     $.ajaxSetup({
//         beforeSend: CSRFpass,
//     });
*/
function CSRFpass(xhr, settings) {
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", $.cookies.get( 'csrftoken'));
    }
}
