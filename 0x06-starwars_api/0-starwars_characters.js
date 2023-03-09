#!/usr/bin/node
const request = require('request');
const SW_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  request(`${SW_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const characters = JSON.parse(body).characters;
    const names = characters.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, body) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(body).name);
        });
      }));

    Promise.all(names)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
