#!/usr/bin/node
const url = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');
request(url, function (error, response, body) {
    if (error) {
        return console.error(error);
    }
    fs.writeFile(file, body, 'utf8', function (err) {
        if (err) {
            return console.error(err);
        }
    });
});
