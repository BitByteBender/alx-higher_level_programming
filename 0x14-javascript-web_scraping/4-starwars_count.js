#!/usr/bin/node
// Script that prints number of movies specified by "Wedge Antilles"
'use_strict';

const req = require('request');

const urlAPI = process.argv[2];

const charID = '18';

req.get(urlAPI, (err, res, cnt) => {
  if (err) {
    console.error(err);
    return;
  }

  const url = `https://swapi-api.alx-tools.com/api/people/${charID}/`;

  const count = JSON.parse(cnt).results.filter(movie => movie.characters.includes(url)).length;

  console.log(count);
});
