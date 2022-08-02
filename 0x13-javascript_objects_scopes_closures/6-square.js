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
			for (x; x < this.size; x++)
				console.log('X'.repeat(this.size));
		}
		else
		{
			for (x; x < this.size; x++)
				console.log('C'.repeat(this.size));
		}
	}
}

module.exports = Square;
