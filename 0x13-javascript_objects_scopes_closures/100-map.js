#!/usr/bin/node

/* script that imports an array and computes a new array */

const data = require('./100-data');

const copy = data.list;
console.log(data.list);
const map1 = data.list.map(x => x * (x - 1));
console.log(map1);
