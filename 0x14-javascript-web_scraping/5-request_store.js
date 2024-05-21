#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.
'use strict';

const req = require('request');
const fsys = require('fs');

const urlAPI = process.argv[2];
const fPath = process.argv[3];

req(urlAPI, (err, res, cnt) => {
  if (err) {
    console.error(err);
    return;
  }

  fsys.writeFile(fPath, cnt, 'utf-8', () => {});
});
