#!/usr/bin/node
const request = require('request');
const moveId = process.argv.slice(2);
let titl;
request('https://swapi-api.hbtn.io/api/films/' + moveId[0],
  (error, response, body) => {
    if (error) console.error('error:', error);
    else {
      titl = JSON.parse(body);
      console.log(titl.title);
    }
  });
