#!/usr/bin/node
const request = require('request');
const files = process.argv.slice(2);
let data;
let count = 0;
request(files[0], (error, response, body) => {
  if (error) console.error('error:', error);
  else {
    data = JSON.parse(body);
    for (const x in data.results) {
      if (data.results[x].characters.filter(y => y.includes('18')).length > 0) { count++; }
    }
    console.log(count);
  }
});
