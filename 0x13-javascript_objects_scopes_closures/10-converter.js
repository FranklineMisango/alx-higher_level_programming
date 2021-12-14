#!/usr/bin/node

exports.converter = function (base) {
  function convert (x) {
    return x.toString(base);
  }
  return convert;
};
