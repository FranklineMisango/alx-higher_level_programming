#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  list.forEach(el => {
    if (el === searchElement) num++;
  });
  return num;
};
