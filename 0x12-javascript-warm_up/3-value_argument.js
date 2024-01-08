#!/usr/bin/node
const [firstArg, ...restArgs] = process.argv.slice(2);

if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
