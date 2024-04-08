#!/usr/bin/node
'use strict';

let increment = 2;

if (process.argv[2] === undefined) {
  console.log(process.argv[increment] + ' is ' + process.argv[++increment]);
} else {
  console.log(process.argv[increment] + ' is ' + process.argv[++increment]);
}
