#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let r = '';
    for (let i = 0; i < this.width; i++) {
      r += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(r);
    }
  }
}

module.exports = Rectangle;
