const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = parseInt(input[0]);
const dp = Array(N + 1).fill(0n);
dp[1] = 1n;

for (let i = 2; i <= N; i++) {
  dp[i] = dp[i - 1] + dp[i - 2];
}
console.log(dp[N].toString());
