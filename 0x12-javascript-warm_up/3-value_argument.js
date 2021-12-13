#!/usr/bin/node

const myArgs = process.argv.length - 2;
const x = process.argv[2];

if (myArgs === 0) {
    console.log('No argument');
} else {
    console.log(x);
}
