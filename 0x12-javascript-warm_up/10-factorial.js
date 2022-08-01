#!/usr/bin/node

/* script that computes and prints a factorial */

const n = process.argv[2];

function factorial (n) {
  if (!n || n === 0) { return 1; } else { return factorial(n - 1) * n; }
}

console.log(factorial(n));
