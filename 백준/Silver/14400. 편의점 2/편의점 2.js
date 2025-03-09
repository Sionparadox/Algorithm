const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = parseInt(input[0]);
const pos = [];

for (let i = 1; i <= N; i++) {
  pos.push(input[i].split(' ').map(Number));
}

const x = pos.map((p) => p[0]);
const y = pos.map((p) => p[1]);

x.sort((a, b) => a - b);
y.sort((a, b) => a - b);
const mid = Math.floor(N / 2);
let ans = 0;
for (let i = 0; i < N; i++) {
  ans += Math.abs(x[i] - x[mid]);
  ans += Math.abs(y[i] - y[mid]);
}
console.log(ans);
