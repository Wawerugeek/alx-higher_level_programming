#!/usr/bin/node
const message = process.argv.length === 2 ? 'No argument' : process.argv.length === 3 ? 'Argument found' : 'Arguments found';
console.log(message);
