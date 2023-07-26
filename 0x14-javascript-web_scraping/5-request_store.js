#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const files = process.argv.slice(2);
request(files[0], (error, res, body) => {
  if (error) console.error('error:', error);
  else {
    fs.writeFile(files[1], body, (err) => {
      if (err) console.log(err);
    });
  }
});
