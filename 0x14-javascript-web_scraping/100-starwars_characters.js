#!/usr/bin/node
const request = require('request');
const files = process.argv.slice(2);
let list = [];
let data;
let i;
function GetCharId (id) {
  request('https://swapi-api.hbtn.io/api/films/' + id,
    async function (error, response, body) {
      if (error) console.error(error);
      else {
        data = JSON.parse(body);
        list = data.characters;
        for (i = 0; i < list.length; i++) {
          const name = await GetName(list[i]);
          console.log(name);
        }
      }
    });
}

function GetName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}
GetCharId(files[0]);
