#!/usr/bin/node
const fs = require('fs')
const files = process.argv.slice(2)
fs.write(files[0], files[1], (err) => {
    if (err) console.log('error', err);
})