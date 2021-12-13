#!/usr/bin/node

const x = process.argv[2];
const y = parseInt(x);

if (isNaN(y)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < y; a++) {
    console.log('X'.repeat(y));
  }
}
