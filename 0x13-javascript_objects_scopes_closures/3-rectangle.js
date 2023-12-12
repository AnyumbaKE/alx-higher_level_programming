#!/usr/bin/node
// A class Rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let y = 0; y < this.height; y++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;