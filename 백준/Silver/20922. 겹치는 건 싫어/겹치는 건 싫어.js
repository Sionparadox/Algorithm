const fs = require('fs');
const input = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map((str) => str.split(' ').map(Number));
// const input = fs
//   .readFileSync('input.txt')
//   .toString()
//   .trim()
//   .split('\n')
//   .map((str) => str.split(' ').map(Number));
const [N, K] = input[0];
const nums = input[1];
let ans = 0;
let s = 0;
let e = 0;
const map = new Map();
map.set(nums[0], 1);
while (s < N && e < N) {
  if (map.get(nums[e]) <= K) {
    e++;
    map.set(nums[e], (map.get(nums[e]) || 0) + 1);
    ans = Math.max(ans, e - s);
  } else {
    map.set(nums[s], map.get(nums[s]) - 1);
    s++;
  }
}
console.log(ans);
