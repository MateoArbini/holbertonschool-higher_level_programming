#!/usr/bin/node

/* script that imports an array and computes a new array */

const data = require('./100-data');

let x = 0;
const new_list = [];
console.log(data.list);
const map1 = data.list.map(x => x * (x - 1)); {
	new_list.push(data.list[x]); }
console.log(map1);
