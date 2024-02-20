#!/usr/bin/node

const fs = require('fs');
const [arg1 = 'undefined', arg2 = 'undefined'] = process.argv.slice(2);

fs.writeFile(arg1, arg2, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
