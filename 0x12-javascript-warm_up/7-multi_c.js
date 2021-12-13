#!/usr/bin/node

const x = 'C is fun';
const y = process.argv[2];
const z = parseInt(y);

if (isNaN(z)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < z; i++) {
    console.log(x);
  }
}
