#!/usr/bin/node
const MyString = process.argv[3];
const Myfile = process.argv[2];
const fs = require('fs');
fs.writeFile(Myfile, MyString, 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
});
