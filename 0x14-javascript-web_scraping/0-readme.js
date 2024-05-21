#!/usr/bin/node
// Script that reads and prints the content of a file
'use_strict';

const fsys = require('fs');

const fPath = process.argv[2];

fsys.readFile(fPath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
