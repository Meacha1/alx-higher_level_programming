#!/usr/bin/node
const FilePath = process.argv[2];
const fs = require('fs');
fs.readFile(FilePath, 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});
