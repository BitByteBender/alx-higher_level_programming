'use strict';
/*
 * Script that fetches from a specified url and display hello into DIV#hello
 * url: https://hellosalut.stefanbohacek.dev/?lang=fr
 * */

const valueURL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(valueURL, function (fetchedData) {
  $('div#hello').text(fetchedData);
});
