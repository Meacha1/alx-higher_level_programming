#!/usr/bin/node
const count = process.argv.length;

if (count === 3) {
  console.log(process.argv[2] + ' is undefined');
}
if (count === 2) {
  console.log('undefined is undefined');
}
if (count === 4) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
