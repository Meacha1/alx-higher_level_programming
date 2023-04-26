#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  const json = JSON.parse(body);
  const completed = {};
  for (const task of json) {
    if (task.completed === true) {
      if (completed[task.userId] === undefined) {
        completed[task.userId] = 1;
      } else {
        completed[task.userId]++;
      }
    }
  }
  console.log(completed);
});
