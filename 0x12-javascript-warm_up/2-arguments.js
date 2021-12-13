#!/usr/bin/node

const myArgs = process.argv.length - 2;
if (myArgs === 0) {
  console.log('No argument');
} else if (myArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
