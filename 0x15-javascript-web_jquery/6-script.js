'use strict';
/*
 * Script that updates the text of the header tag element
 * to New Header!!! when the user clicks on DIV#update_header
 * */

$('div#update_header').click(function () {
  $('header').text('New Header!!!');
});
