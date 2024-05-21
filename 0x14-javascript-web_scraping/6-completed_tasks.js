#!/usr/bin/node
// Script that prints number of movies specified by "Wedge Antilles"
'use strict';

const req = require('request');

const urlAPI = process.argv[2];

req(urlAPI, (err, res, cnt) => {
  if (err) {
    console.error(err);
    return;
  }

  const doneTasks = JSON.parse(cnt).reduce((cpt, td) => {
    if (td.completed) {
      cpt[td.userId] = (cpt[td.userId] || 0) + 1;
    }
    return (cpt);
  }, {});

  const formattedOutput = Object.entries(doneTasks).map(([k, val]) => `  '${k}': ${val}`).join(',\n');
  console.log(`{${formattedOutput} }`);
});
