const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = parseInt(input[0]);
const view = input.slice(1).map((item) => item.split(' ').map(Number));

const stack = [];
let ans = 0;
for (const [_, y] of view) {
  while (stack.length > 0 && stack.at(-1) > y) {
    stack.pop();
    ans++;
  }
  if (y != 0 && (stack.length == 0 || stack.at(-1) != y)) {
    stack.push(y);
  }
}
console.log(ans + stack.length);
