#!/usr/bin/node

const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
    this.print(c);
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
