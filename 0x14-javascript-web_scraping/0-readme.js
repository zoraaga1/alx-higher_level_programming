#!/usr/bin/node

const fs = require('fs');
const [firstArg] = process.argv.slice(2);

fs.readFile(firstArg, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
