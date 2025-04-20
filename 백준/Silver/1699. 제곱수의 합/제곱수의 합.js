const fs = require('fs');
const N = +fs.readFileSync(0, 'utf-8').toString().trim();

const dp = Array(N+1).fill(0);


for (let i=1; i<=N; i++){
    let minVal = Infinity;
    for (let j=1; j <= Math.sqrt(i); j++){
        minVal = Math.min(minVal, dp[i - j * j]);
    }
    dp[i] = minVal + 1;
}
console.log(dp[N]);
