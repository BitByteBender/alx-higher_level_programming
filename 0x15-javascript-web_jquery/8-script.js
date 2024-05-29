'use strict';
/*
 * Script that fetches and lists title for all movies from a specified url
 * url: https://swapi-api.alx-tools.com/api/films/?format=json
 * */

const moviesURL = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(moviesURL, function (fetchedData) {
  fetchedData.results.forEach(function (movie) {
    $('ul#list_movies').append(`<li>${movie.title}</li>`);
  });
});
