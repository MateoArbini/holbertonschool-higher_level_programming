#!/usr/bin/node

/* function that returns the reversed version of a list */

exports.esrever = function (list) {
  const rev = [];
  let x = list.length - 1;
  for (x; x >= 0; x--) {
    rev.push(list[x]);
  }
  return rev;
};
