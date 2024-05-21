#!/usr/bin/node
// Script that prints all actors of Star Wars movie in same order of the list
'use strict';

const req = require('request');

const mvID = process.argv[2];

const urlEndpoint = `https://swapi-api.alx-tools.com/api/films/${mvID}`;

req.get(urlEndpoint, (err, res, cnt) => {
  if (err) {
    console.error(err);
    return;
  }

  const mv = JSON.parse(cnt); const chr = mv.characters;

  const retrieveCharName = (characterUrl) => {
    req(characterUrl, (err, res, cnt) => {
      if (err) {
        console.error(err);
        return;
      }

      console.log(JSON.parse(cnt).name);
    });
  };

  const procChr = async () => {
    for (const characterUrl of chr) {
      await new Promise(resolve => {
        retrieveCharName(characterUrl);
        resolve();
      });
    }
  };

  procChr();
});
