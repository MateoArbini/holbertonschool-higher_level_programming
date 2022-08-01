#!/usr/bin/node

/*  function that increments and calls a function */

exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  let y = 0;
  let nb = 0;
  for (y; y <= number; y++) {
    nb = nb + 1;
  }
  theFunction(nb);
};
