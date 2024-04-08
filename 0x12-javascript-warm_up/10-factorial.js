#!/usr/bin/node
'use strict';

const val = parseInt(process.argv[2]);

if (isNaN(val)) {
  console.log(1);
} else {
  function recursiveFactorial (a) {
    if (a === 1 || a === 0) {
      return (1);
    } else {
      return (a * recursiveFactorial(a - 1));
    }
  }

  console.log(recursiveFactorial(val));
}
