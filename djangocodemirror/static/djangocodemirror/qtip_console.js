/*
 * Console log for DjangoCodeMirror
 *
 * Use qTip to emulate jGrowl behaviour
*/
GROWL_KINDS = {
    'success': 'ui-tooltip-green',
    'info': 'ui-tooltip-blue',
    'error': 'ui-tooltip-red',
    'warning': 'ui-tooltip-red',
};

window.createGrowl = function(element_instance, kind, title, message, persistent) {
    // Use the last visible jGrowl qtip as our positioning target
    var target = $('.qtip.jgrowl:visible:last');
    // Create the jGrowl relatively positioned
    $(".CodeMirror-lines", element_instance).qtip({
        // Any content config you want here really.... go wild!
        content: {
            text: message,
            title: {
                text: title,
                button: true
            }
        },
        position: {
            my: 'top right', // Not really important...
            at: (target.length ? 'bottom' : 'top') + ' right', // If target is window use 'top right' instead of 'bottom right'
            target: target.length ? target : $(element_instance), // Use our target declared above
            adjust: { y:5 } // Add some vertical spacing
        },
        show: {
            event: false, // Don't show it on a regular event
            ready: true, // Show it when ready (rendered)
            effect: function() { $(this).stop(0,1).fadeIn(400); }, // Matches the hide effect
            delay: 0, // Needed to prevent positioning issues
            
            // Custom option for use with the .get()/.set() API, awesome!
            persistent: persistent
        },
        hide: {
            event: false, // Don't hide it on a regular event
            effect: function(api) { 
            // Do a regular fadeOut, but add some spice!
            $(this).stop(0,1).fadeOut(400).queue(function() {
                // Destroy this tooltip after fading out
                api.destroy();

                // Update positions
                updateGrowls(element_instance);
            })
            }
        },
        style: {
            classes: 'jgrowl '+ GROWL_KINDS[kind] +' ui-tooltip-rounded ui-tooltip-shadow ui-tooltip-console', // Some nice visual classes
            tip: false // No tips for this one (optional ofcourse)
        },
        events: {
            render: function(event, api) {
            // Trigger the timer (below) on render
            jGrowl_timer.call(api.elements.tooltip, event);
            }
        }
    })
    .removeData('qtip');
};

// Make it a window property see we can call it outside via updateGrowls() at any point
window.updateGrowls = function(element_instance) {
    // Loop over each jGrowl qTip
    var each = $('.qtip.jgrowl:not(:animated)');
    each.each(function(i) {
        var api = $(this).data('qtip');

        // Set the target option directly to prevent reposition() from being called twice.
        api.options.position.target = !i ? $(element_instance) : each.eq(i - 1);
        api.set('position.at', (!i ? 'top' : 'bottom') + ' right');
    });
};

// Setup our timer function
function jGrowl_timer(event) {
    var api = $(this).data('qtip'),
        lifespan = 4000; // 4 second lifespan
    
    // If persistent is set to true, don't do anything.
    if(api.get('show.persistent') === true) { return; }

    // Otherwise, start/clear the timer depending on event type
    clearTimeout(api.timer);
    if(event.type !== 'mouseover') {
        api.timer = setTimeout(api.hide, lifespan);
    }
}

// Utilise delegate so we don't have to rebind for every qTip!
$(document).delegate('.qtip.jgrowl', 'mouseover mouseout', jGrowl_timer);
