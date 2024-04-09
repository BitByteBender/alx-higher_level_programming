#!/usr/bin/node

'use strict';

exports.converter = function (base) {
  return (number) => {
    return (number.toString(base));
  };
};
