#!/usr/bin/node

'use strict';
const sSquare = require('./5-square');

class Square extends sSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    while (i < this.height) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
      i++;
    }
  }
}

module.exports = Square;
