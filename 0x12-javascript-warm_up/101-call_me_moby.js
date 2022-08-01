#!/usr/bin/node

/* function that executes x times a function */

exports.callMeMoby = function callMeMoby (x, theFunction) {
  let y = 0;
  for (y; y < x; y++) {
    theFunction();
  }
};
