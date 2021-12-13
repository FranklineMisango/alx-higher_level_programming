#!/usr/bin/node

const x = process.argv[2];
const y = parseInt(x);

if (isNaN(y)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + y);
}
