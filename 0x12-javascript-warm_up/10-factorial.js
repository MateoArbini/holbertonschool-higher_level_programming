#!/usr/bin/node

/* script that computes and prints a factorial */

const n = process.argv[2];

function factorial (n) {
  let result = n;

  if (!n) { return 1; }
  if (n === 0 || n === 1) { return 1; }
  while (n > 1) {
    n--;
    result *= n;
  }
  return result;
}

console.log(factorial(n));
