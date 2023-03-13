#!/usr/bin/node
const i = parseInt(process.argv[2]);
if (isNaN(i)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + i);
}
