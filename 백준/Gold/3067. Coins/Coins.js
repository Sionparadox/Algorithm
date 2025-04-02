const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const T = +input[0];

for (let t = 0; t < T; t++) {
  const N = +input[3 * t + 1];
  const coins = input[3 * t + 2].split(' ').map(Number);
  const M = +input[3 * t + 3];

  const dp = Array(M + 1).fill(0);
  dp[0] = 1;
  for (const coin of coins) {
    for (let i = coin; i <= M; i++) {
      dp[i] += dp[i - coin];
    }
  }
  console.log(dp[M]);
}
