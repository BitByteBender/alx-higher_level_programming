#!/usr/bin/node
// Script that prints number of tasks completed by user id
'use strict';

const req = require('request');

const urlAPI = process.argv[2];

req.get(urlAPI, (err, res, cnt) => {
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

  console.log(JSON.stringify(doneTasks, null, 2));
});
