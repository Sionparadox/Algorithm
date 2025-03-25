const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [A, B, C, N] = input[0].split(' ').map(Number);

const dp = Array(N + 1).fill(false);
dp[0] = true;

for (const i of [A, B, C]) {
  for (let j = i; j <= N; j++) {
    if (dp[j - i]) {
      dp[j] = true;
    }
  }
}
console.log(dp[N] ? 1 : 0);
