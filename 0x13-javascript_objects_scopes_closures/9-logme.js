#!/usr/bin/node
// This script is for a function that prints the number of arguments already printed and the new argument value
let count = 0;
exports.logMe = function (item) { console.log(`${count++}: ${item}`); };
