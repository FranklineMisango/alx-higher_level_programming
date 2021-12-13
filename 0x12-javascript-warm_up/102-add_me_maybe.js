#!/usr/bin/node

module.exports = {
  addMeMaybe: function (a, b) {
    return b(a + 1);
  }
};
