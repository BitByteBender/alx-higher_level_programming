#!/usr/bin/node
// Script that reads and prints the content of a file
'use_strict';

const fsys = require('fs');

const fPath = process.argv[2];
const cnt = process.argv[3];

fsys.writeFile(fPath, cnt, 'utf-8', () => {});
