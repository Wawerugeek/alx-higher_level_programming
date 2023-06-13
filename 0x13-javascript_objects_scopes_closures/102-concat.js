#!/usr/bin/node
const fs = require('fs');

const concatFiles = (file1, file2, file3) => {
  const file1C = fs.readFileSync(file1, 'utf8');
  const file2C = fs.readFileSync(file1, 'utf8');
  const concat = file1C + file2C;
  fs.writeFileSync(file3, concat);
};
const file1 = process.argv[2];
const file2 = process.argv[3];
const concat = process.argv[4];

concatFiles(file1, file2, concat);
