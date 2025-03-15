const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const T = parseInt(input[0]);
for (let t=0;t<T;t++){
    const N = parseInt(input[t*3+1]);
    const field = input.slice(t*3+2,t*3+4).map(item => item.split(' ').map(Number));
    const dp = Array(2).fill().map(() => Array(N+1).fill(0));
    dp[0][1] = field[0][0];
    dp[1][1] = field[1][0];
    for (let i=2;i<=N;i++){
        dp[0][i] = Math.max(dp[1][i-1],dp[1][i-2],dp[0][i-2]) + field[0][i-1];
        dp[1][i] = Math.max(dp[0][i-1],dp[1][i-2],dp[0][i-2]) + field[1][i-1];
    }
    console.log(Math.max(dp[0][N], dp[1][N]));
}