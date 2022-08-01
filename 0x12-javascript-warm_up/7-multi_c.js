#!/usr/bin/node

/* script that prints x times “C is fun” */

const text = 'C is fun';
const x = process.argv[2];
let y = 0;

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else { parseInt(x); }

for (y; y < x; y++) {
  console.log(text);
}
