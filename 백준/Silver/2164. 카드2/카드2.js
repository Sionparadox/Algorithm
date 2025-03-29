const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();
// const input = fs.readFileSync('input.txt').toString().trim();
const N = +input;

const arr = Array.from({ length: N }, (_, i) => i + 1);
let idx = 0;
while (idx < arr.length - 1) {
  arr.push(arr[idx + 1]);
  idx += 2;
}
console.log(arr.at(-1));
