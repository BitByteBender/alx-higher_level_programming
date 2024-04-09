#!/usr/bin/node

'use strict';
let logger = 0;

exports.logMe = function (item) {
  console.log(logger + ': ' + item);
  logger++;
};
