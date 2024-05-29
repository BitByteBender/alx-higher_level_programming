'use strict';
/*
 * Script that fetches the character name from a specified url
 * url: https://swapi-api.alx-tools.com/api/people/5/?format=json
 * */

const chrURL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(chrURL, function (fetchedData) {
  $('div#character').text(fetchedData.name);
});
