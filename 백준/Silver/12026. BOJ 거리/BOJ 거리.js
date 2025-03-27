const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = +input[0];
const road = input[1];

const BOJ = {
  B: [],
  O: [],
  J: [],
};

for (let i = 0; i < N; i++) {
  BOJ[road[i]].push(i);
}

const dp = Array(N).fill(Infinity);
dp[0] = 0;
for (let i = 0; i < N; i++) {
  const temp = BOJ[next(road[i])];
  for (const pos of temp) {
    if (pos < i) continue;
    dp[pos] = Math.min(dp[pos], dp[i] + Math.pow(pos - i, 2));
  }
}
console.log(dp[N - 1] == Infinity ? -1 : dp[N - 1]);

function next(a) {
  if (a == 'B') return 'O';
  if (a == 'O') return 'J';
  if (a == 'J') return 'B';
}
