const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = +input[0];
const M = +input[1];
const arr = (input[2] || '').split(' ').map(Number);
const btn = [];

for (let i = 0; i < 10; i++) {
  if (M == 0 || !arr.includes(i)) {
    btn.push(i);
  }
}

let ans = Math.abs(N - 100);
for (let i = -1; i <= 1; i++) {
  const len = input[0].length;
  if (len + i <= 0) continue;
  dfs('', len + i);
}
console.log(ans);

function dfs(n, k) {
  if (n.length >= k) {
    ans = Math.min(ans, n.length + Math.abs(+n - N));
    return;
  }
  for (const i of btn) {
    dfs(n + i, k);
  }
}
