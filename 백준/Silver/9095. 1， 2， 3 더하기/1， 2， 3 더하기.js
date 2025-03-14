const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const T = parseInt(input[0]);

const dp = Array(12).fill(0);
dp[0] = 0;
dp[1] = 1;
dp[2] = 2;
dp[3] = 4;
for (let i=4;i<12;i++){
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1];
}
for (const v of input.slice(1)){
    console.log(dp[v]);
}