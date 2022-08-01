#!/usr/bin/node

/* script that searches the second biggest integer in the list of arguments */

const lista = [];
let unicos = [];
let x = 2;

for (x; x < process.argv.length; x++) {
  lista.push(process.argv[x]);
}
lista.sort();
unicos = [...new Set(lista)];

if (unicos.length === 1 || !process.argv[2]) {
  console.log('0');
} else {
  console.log(unicos[unicos.length - 2]);
}
