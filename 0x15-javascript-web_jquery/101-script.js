'use strict';

$(document).ready(function () {
  const tag = 'ul.my_list';
  $('div#add_item').click(function () {
    $(tag).append('<li>Item</li>');
  });

  $('div#remove_item').click(function () {
    $(tag + ' li:last-child').remove();
  });

  $('div#clear_list').click(function () {
    $(tag).empty();
  });
});
