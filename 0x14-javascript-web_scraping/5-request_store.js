#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(`The contents of the webpage have been saved to ${filePath}`);
  });
});
