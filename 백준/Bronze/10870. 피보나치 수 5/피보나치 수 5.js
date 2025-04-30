const fs = require('fs');
const N = +fs.readFileSync(0, 'utf-8').toString().trim();
const dp = Array(N+1).fill(0);
dp[1] = dp[2] = 1;

for (let i=2; i<=N; i++){
    dp[i] = dp[i-1] + dp[i-2];
}
console.log(dp[N]);
