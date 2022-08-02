#!/usr/bin/node

/* prints the number of arguments already printed and the new argument value. (see example below) */

const log = [];

exports.logMe = function (item) {
	log.push(item);
	console.log(log.length - 1 + ":" + " " + item);
};
