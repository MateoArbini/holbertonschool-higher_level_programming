#!/usr/bin/node

/* class Square that defines a square and inherits from Rectangle of 4-rectangle.js */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
	constructor(size) {
		super(size, size);
	}
	charPrint (c = 'X') {
		let x = 0;
		for (x; x < this.width; x++)
			console.log(c.repeat(this.height));
	}
}

module.exports = Square;
