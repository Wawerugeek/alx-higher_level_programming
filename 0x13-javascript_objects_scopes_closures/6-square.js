#!/usr/bin/node
const Square0 = require('./5-square');
class Square extends Square0 {
  charPrint (char) {
    const character = char || 'X';
    let r = '';
    for (let i = 0; i < this.width; i++) {
      r += character;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(r);
    }
  }
}

module.exports = Square;
