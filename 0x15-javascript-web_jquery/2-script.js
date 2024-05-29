'use strict';
/*
 * Script that updates text color of the header to red
 * when user clicks on DIV#red_header tag
 * */

$('div#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
