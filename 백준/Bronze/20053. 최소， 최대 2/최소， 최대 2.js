const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const T = +input[0];
let line = 1;
const ans = [];
for (let t = 0; t < T; t++) {
  const N = +input[line++];
  const arr = input[line++].split(' ').map(Number);
  ans.push(Math.min(...arr) + ' ' + Math.max(...arr));
}
console.log(ans.join('\n'));
