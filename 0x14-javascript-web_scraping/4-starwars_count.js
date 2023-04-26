#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const json = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < json.results.length; i++) {
    for (let j = 0; j < json.results[i].characters.length; j++) {
      if (json.results[i].characters[j].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
