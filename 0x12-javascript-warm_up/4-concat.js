#!/usr/bin/node

/* script print 2 arguments passed, in the following format: “ is ” */

const myVar1 = process.argv[2];
const myVar2 = process.argv[3];

if (!myVar1 && !myVar2) {
  console.log('undefined is undefined');
} else if (myVar1 === '' && !myVar2) {
  console.log(myVar1 + ' ' + 'is undefined');
} else {
  console.log(myVar1 + ' ' + 'is' + ' ' + myVar2);
}
