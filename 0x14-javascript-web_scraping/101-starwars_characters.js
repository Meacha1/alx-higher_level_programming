#!/usr/bin/node
const movie_id = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + movie_id;
request(url, function (error, response, body) {
    if (error) {
        return console.log(error);
    }
    const json = await.JSON.parse(body);
    const characters = await.json.characters;
    for (let i = 0; i < characters.length; i++) {
        request(characters[i], function (error, response, body) {
            if (error) {
                return console.log(error);
            }
            const json = await.JSON.parse(body);
            await.console.log(json.name);
        });
    }
});
