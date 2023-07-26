#!/usr/bin/node
const request = require('request');
const files = process.argv.slice(2);
const dct = {};
let data;
request(files[0], (error, res, body) => {
  if (error) console.error('error:', error);
  else {
    data = JSON.parse(body);
    for (const x in data) {
      if (data[x].completed === true) {
        if (!(data[x].userId in dct)) { dct[data[x].userId] = 1; } else { dct[data[x].userId] += 1; }
      }
    }
    console.log(dct);
  }
});
