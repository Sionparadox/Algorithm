const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, L, R, X] = input[0].split(' ').map(Number);
const levels = input[1].split(' ').map(Number);

levels.sort((a, b) => a - b);

let cnt = 0;
backtrack(0, []);
console.log(cnt);

function backtrack(idx, arr) {
  const total = arr.reduce((acc, v) => acc + v, 0);
  if (total > R) return;

  if (idx == N) {
    if (arr.length > 1 && total >= L && total <= R && arr.at(-1) - arr[0] >= X)
      cnt++;
    return;
  }

  backtrack(idx + 1, [...arr, levels[idx]]);
  backtrack(idx + 1, arr);
}
