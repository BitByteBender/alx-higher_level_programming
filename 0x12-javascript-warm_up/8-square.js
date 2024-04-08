#!/usr/bin/node
'use strict';

const x = process.argv[2];

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let line = '';

    for (let j = 0; j < x; j++) {
      line = line + 'X';
    }
    console.log(line);
  }
}
