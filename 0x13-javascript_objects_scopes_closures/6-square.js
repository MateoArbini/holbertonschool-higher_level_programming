#!/usr/bin/node

/* class Square that defines a square and inherits from Rectangle of 4-rectangle.js */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
	constructor(size) {
		super(size, size);
		this.size = size;
	}
	charPrint (c) {
		let x = 0;
		if (c === undefined)
		{
			for (x; x < this.width; x++)
				console.log('X'.repeat(this.height));
		}
		else
		{
			for (x; x < this.width; x++)
				console.log('C'.repeat(this.height));
		}
	}
}

module.exports = Square;
