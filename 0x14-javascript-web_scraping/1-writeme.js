#!/usr/bin/node
// Script that writes into a file
'use strict';

const fsys = require('fs');

const fPath = process.argv[2];
const cnt = process.argv[3];

fsys.writeFile(fPath, cnt, 'utf-8', () => {});
