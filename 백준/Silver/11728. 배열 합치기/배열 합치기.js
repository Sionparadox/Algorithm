const fs = require('fs');
const input = fs.readFileSync(0,'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const A = input[1].split(' ').map(Number);
const B = input[2].split(' ').map(Number);
const arr = [...A, ...B];
arr.sort((a, b) => a - b);
console.log(arr.join(' '));
