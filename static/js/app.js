$(document).ready(function() {
    'use strict';

    // fade in #back-top
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('#back-top').fadeIn();
        } else {
            $('#back-top').fadeOut();
        }
    });

    // scroll body to 0px on click
    $('#back-top a').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });

    // display certificate fingerprint
    $('#fingerprint').load('fingerprint.html');
});
