#!/usr/bin/node
'use strict';

let array = process.argv.slice(2);

if (process.argv.length <= 3) {
  console.log('0');
} else {
  array = array.map(Number);
  array.sort(function (val1, val2) {
    return (val2 - val1);
  }
  );
  console.log(array[1]);
}
