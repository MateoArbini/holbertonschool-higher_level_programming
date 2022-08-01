#!/usr/bin/node

/* script that prints the addition of 2 integers */

const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  const a1 = parseInt(a);
  const b2 = parseInt(b);
  const result = a1 + b2;
  console.log(result);
}

add(a, b);
