#!/usr/bin/node
const movieId = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
