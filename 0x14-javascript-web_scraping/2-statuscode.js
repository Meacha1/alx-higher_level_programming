#!/usr/bin/node
const link = process.argv[2];
const request = require('request');
request(link, function (error, response) {
  if (error) {
    return console.log(error);
  }
  console.log(`code: ${response.statusCode}`);
});
