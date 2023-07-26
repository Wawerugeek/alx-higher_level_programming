#!/usr/bin/node
const fileSy = require('fs');
const files = process.argv.slice(2)
fileSy.readFile(files[0], 'utf8', (err, data) => {
    if(err) console.log(err);
    else process.stdout.write(data)
} )