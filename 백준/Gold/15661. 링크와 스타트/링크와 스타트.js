const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = parseInt(input[0]);
const S = input.slice(1).map((i) => i.split(' ').map(Number));

let ans = Infinity;
for (let i = 1; i < N; i++) {
  makeCombine(0, [], i);
}
console.log(ans);

function makeCombine(idx, arr, size) {
  if (arr.length == size) {
    ans = Math.min(ans, calcDiff(arr));
    return;
  }

  if (idx + (size - arr.length) > N) return;

  arr.push(idx);
  makeCombine(idx + 1, arr, size);
  arr.pop();
  makeCombine(idx + 1, arr, size);
}

function calcDiff(start) {
  const link = [];
  for (let i = 0; i < N; i++) {
    if (start.includes(i)) continue;
    link.push(i);
  }
  let s = 0;
  let l = 0;
  for (let i = 0; i < start.length; i++) {
    for (let j = 0; j < start.length; j++) {
      s += S[start[i]][start[j]];
    }
  }

  for (let i = 0; i < link.length; i++) {
    for (let j = 0; j < link.length; j++) {
      l += S[link[i]][link[j]];
    }
  }
  return Math.abs(s - l);
}
