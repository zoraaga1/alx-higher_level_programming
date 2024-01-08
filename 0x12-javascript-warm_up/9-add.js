#!/usr/bin/node

function add (a, b) {
  console.log(Number(a) + Number(b));
}

const [arg1, arg2] = process.argv.slice(2);

add(arg1, arg2);
