#!/usr/bin/node
const factorial = (n) => (n === 1 || isNaN(n)) ? 1 : (n * factorial(n - 1));
console.log(factorial(parseInt(process.argv[2])));
