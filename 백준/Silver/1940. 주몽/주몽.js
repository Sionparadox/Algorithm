const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = parseInt(input[0]);
const M = parseInt(input[1]);
const nums = input[2].split(' ').map(Number);

nums.sort((a, b) => a - b);
let s = 0;
let e = N - 1;
let ans = 0;
while (s < e) {
  if (nums[s] + nums[e] == M) {
    ans++;
    s++;
    e--;
  } else if (nums[s] + nums[e] > M) {
    e--;
  } else {
    s++;
  }
}

console.log(ans);
