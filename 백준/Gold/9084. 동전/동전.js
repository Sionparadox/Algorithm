const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const T = parseInt(input[0]);
for (let t = 1; t <= T; t++) {
  const N = parseInt(input[t * 3 - 2]);
  const coins = input[t * 3 - 1].split(' ').map(Number);
  const price = parseInt(input[t * 3]);
  const dp = Array(price + 1).fill(0);
  dp[0] = 1;
  for (const c of coins) {
    for (let p = c; p <= price; p++) {
      dp[p] += dp[p - c];
    }
  }
  console.log(dp[price]);
}
