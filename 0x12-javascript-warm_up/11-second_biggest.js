#!/usr/bin/node

/* script that searches the second biggest integer in the list of arguments */

const lista = [];
let x = 2;

if (!process.argv[2] || process.argv[2] == 1 || process.argv[2] == 0) {
  console.log('0');
} else {
  for (x; x < process.argv.length; x++) {
    lista.push(process.argv[x]);
  }
  lista.sort();
  console.log(lista[lista.length - 2]);
}
