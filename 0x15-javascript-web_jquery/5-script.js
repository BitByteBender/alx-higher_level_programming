'use strict';
/*
 * Script that adds a <li> element to a list
 * when user clicks on DIV#add_item tag
 * */

$('div#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
