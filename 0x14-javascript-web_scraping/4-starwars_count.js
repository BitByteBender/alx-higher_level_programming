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

  const DoneMovieCount = JSON.parse(cnt).results.reduce((count, movie) =>
    movie.characters.some(chr => chr.includes(charID)) ? (count + 1) : count, 0);

  console.log(DoneMovieCount);
});
