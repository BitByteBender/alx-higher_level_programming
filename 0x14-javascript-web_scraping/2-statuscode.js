#!/usr/bin/node
// Script that prints the status code of a url
'use strict';

const req = require('request');

const urlArg = process.argv[2];

req.get(urlArg, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
