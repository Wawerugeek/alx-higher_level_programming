#!/usr/bin/node
const request = require('request');
const files = process.argv.slice(2);
request(files[0], (error, response) => {
  if (error) console.error('error', error);
  console.log('code:', response.statusCode);
});
