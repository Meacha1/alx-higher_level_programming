#!/usr/bin/node
const num = Number(process.argv[2]);

if (process.argv[2] == null || isNaN(num)) {
  console.log('Missing size');
}

for (let i = 0; i < num; i++) {
  let tmp = '';
  for (let j = 0; j < num; j++) {
    tmp = tmp + 'X';
  }
  console.log(tmp);
}
