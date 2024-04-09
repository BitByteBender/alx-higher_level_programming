#!/usr/bin/node
'use strict';

exports.callMeMoby = (number, theFunction) => {
  theFunction(number++);
};
