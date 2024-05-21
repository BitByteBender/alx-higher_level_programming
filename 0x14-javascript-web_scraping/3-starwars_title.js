#!/usr/bin/node
// Script that prints title of a Star Wars movie via its ID
'use strict';

const req = require('request');

const mvID = process.argv[2];

const urlEndpoint = `https://swapi-api.alx-tools.com/api/films/${mvID}`;

req.get(urlEndpoint, (err, res, cnt) => {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(cnt).title);
  }
});
