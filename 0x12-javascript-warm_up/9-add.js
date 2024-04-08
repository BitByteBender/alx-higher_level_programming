#!/usr/bin/node
'use strict';

const val1 = process.argv[2];
const val2 = process.argv[3];

if (isNaN(val1) || isNaN(val2)) {
  console.log('NaN');
} else {
  function add (a, b) {
    console.log(a + b);
  }

  add(val1, val2);
}
