#!/usr/bin/node
'use strict';

const line = 'C is fun';
const x = process.argv[2];

if (x !== undefined) {
  for (let i = 0; i < x; i++) {
    console.log(line);
  }
} else {
  console.log('Missing number of occurrences');
}
