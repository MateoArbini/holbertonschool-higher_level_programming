#!/usr/bin/node

/* Write a function that returns the number of occurrences in a list */

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let x = 0;
  for (x; x < list.length; x++) {
    if (list[x] === searchElement) {
      count += 1;
    }
  }
  return count;
};
