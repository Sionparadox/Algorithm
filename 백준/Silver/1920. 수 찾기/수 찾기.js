const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');

const A = input[1].split(' ').map(Number);
const nums = input[3].split(' ').map(Number);

const set = new Set(A);
for (const n of nums) {
  console.log(set.has(n) ? 1 : 0);
}
