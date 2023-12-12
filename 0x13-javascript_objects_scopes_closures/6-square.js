#!/usr/bin/node
// A class Square that defines a square and inherits from Square of 5-square.js
const square = require('./5-square');
module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
