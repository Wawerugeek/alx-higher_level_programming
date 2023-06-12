#!/usr/bin/node
const input = process.argv.slice(2).sort((a, b) => a - b);
!isNaN(input[1]) ? console.log(input[input.length - 2]) : console.log('0');
