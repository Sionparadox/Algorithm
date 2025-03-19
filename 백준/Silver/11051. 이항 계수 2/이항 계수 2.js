const fs = require('fs');
const [N, K] = fs
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split(' ')
  .map(Number);

const dp = Array(N + 1)
  .fill()
  .map(() => Array(N + 1).fill(0));

for (let i = 0; i <= N; i++) {
  dp[i][0] = 1;
  dp[i][i] = 1;
}

for (let i = 2; i <= N; i++) {
  for (let j = 1; j < i; j++) {
    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 10007;
  }
}
console.log(dp[N][K]);
