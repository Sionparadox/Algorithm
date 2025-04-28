const fs = require('fs');
const N = +fs.readFileSync(0, 'utf-8').toString().trim();

const dp = Array(N+1).fill(Infinity);
dp[N] = 0;

for (let i=N; i>=1; i--){
    if(i % 3 == 0) dp[i/3] = Math.min(dp[i/3], dp[i]+1);
    if(i % 2 == 0) dp[i/2] = Math.min(dp[i/2], dp[i]+1);
    dp[i-1] = Math.min(dp[i-1], dp[i]+1);
}
console.log(dp[1]);