#!/usr/bin/node

function factorial (n) {
  const N = Number(n);
  if (isNaN(N) || N === 1) {
    return 1;
  } else {
    return N * factorial(N - 1);
  }
}

const arg = process.argv[2];

console.log(factorial(arg));
