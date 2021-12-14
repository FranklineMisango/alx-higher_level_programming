#!/usr/bin/node

const list = require('./101-data').dict;
const list2 = {};

Object.keys(list).forEach(key => {
  if (list2[list[key]] === undefined) list2[list[key]] = [];
  list2[list[key]].push(key);
}
);

console.log(list2);
