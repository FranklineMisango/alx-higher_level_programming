#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(h) || isNaN(w)) return;
    this.width = w;
    this.height = h;
  }
};
