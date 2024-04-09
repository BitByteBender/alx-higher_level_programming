#!/usr/bin/node
'use strict';

exports.addMeMaybe = (number, theFunction) => {
  theFunction(number++);
};
