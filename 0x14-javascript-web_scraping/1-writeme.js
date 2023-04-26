#!/usr/bin/node
const MyString = process.argv[3];
const fs = require('fs');
fs.writeFile('my_file.txt', MyString, 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
});
