#!/usr/bin/node
// A script that reads and prints the content of a file.

const fs = require('fs');

const file = process.argv[2];
const content = process.argv[3];
fs.writeFile(file, content, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});