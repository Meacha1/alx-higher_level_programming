#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const wedgeAntillesId = '18';
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const json = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < json.results.length; i++) {
    for (let j = 0; j < json.results[i].characters.length; j++) {
      if (json.results[i].characters[j].includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}`)) {
        count++;
      }
    }
  }
  console.log(count);
});
