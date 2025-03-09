const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = parseInt(input[0]);
const M = parseInt(input[1]);

const arr = Array.from(Array(N), () => Array(N).fill(0));
let ans = [0, 0];
let depth = 0;
const center = Math.ceil(N / 2);
let r = center;
let c = center;
for (var i = 1; i <= N ** 2; i++) {
  arr[r - 1][c - 1] = i;
  if (i == M) {
    ans = [r, c];
  }
  if (c == center - depth) {
    if (r == center - depth) depth++;
    r--;
  } else if (r == center + depth) {
    c--;
  } else if (c == center + depth) {
    r++;
  } else {
    c++;
  }
}

var res = '';
for (var i = 0; i < N; i++) {
  res += arr[i].join(' ');
  res += '\n';
}
console.log(res + ans.join(' ') + '\n');
