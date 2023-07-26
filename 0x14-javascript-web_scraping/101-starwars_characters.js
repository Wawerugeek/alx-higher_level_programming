#!/usr/bin/node
const request = require('request');
const files = process.argv.slice(2);
const dct = {};
let data;
request(files[0], function (error, res, body) {
  if (error) console.error('error:', error);
  else {
    data = JSON.parse(body);
    for (const i in data) {
      if (data[i].completed === true) {
        if (!(data[i].userId in dct)) { dct[data[i].userId] = 1; } else { dct[data[i].userId] += 1; }
      }
    }
    console.log(dct);
  }
});