#!/usr/bin/node

/* class Rectangle that defines a rectangle */

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let x = 0;
    for (x; x < this.height; x++) { console.log('X'.repeat(this.width)); }
  }
}

module.exports = Rectangle;
