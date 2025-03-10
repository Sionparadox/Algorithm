const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, C, F] = input[0].split(' ').map(Number);
const orders = input.slice(1).map((item) => item.split(' ').map(Number));

const dp = Array(N + 1)
  .fill()
  .map(() =>
    Array(C + 1)
      .fill()
      .map(() => Array(F + 1).fill(0))
  );

for (let i = 1; i <= N; i++) {
  const [cheese, fri] = orders[i - 1];

  for (let c = 0; c <= C; c++) {
    for (let f = 0; f <= F; f++) {
      dp[i][c][f] = dp[i - 1][c][f];
      if (c >= cheese && f >= fri) {
        dp[i][c][f] = Math.max(dp[i][c][f], dp[i - 1][c - cheese][f - fri] + 1);
      }
    }
  }
}
console.log(dp[N][C][F]);
