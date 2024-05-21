#!/usr/bin/node
// Script that prints number of movies specified by "Wedge Antilles"
'use strict';

const req = require('request');

const urlAPI = process.argv[2];

const charID = '18';

req(urlAPI, (err, res, cnt) => {
  if (err) {
    console.error(err);
    return;
  }

  const url = `https://swapi-api.alx-tools.com/api/people/${charID}/`;

  const DoneMovieCount = JSON.parse(cnt).results.reduce((count, movie) =>
    movie.characters.includes(url) ? (count + 1) : count, 0);

  console.log(DoneMovieCount);
});
