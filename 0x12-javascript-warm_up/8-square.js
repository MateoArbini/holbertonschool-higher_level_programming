#!/usr/bin/node

/* script that prints a square */

const size = process.argv[2];
const x = 'X';
let y = 0;

if (isNaN(size)) {
  console.log('Missing size');
} else { parseInt(size); }

for (y; y < size; y++) {
  console.log(x.repeat(size));
}
