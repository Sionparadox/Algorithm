const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = parseInt(input[0]);
const costs = input.slice(1).map(v => v.split(' ').map(Number));

const dp = Array(N).fill().map(() => Array(3).fill(0));
let minCost = Infinity;
for (let c=0;c<3;c++){
    dp[0] = [Infinity, Infinity, Infinity];
    dp[0][c] = costs[0][c];
    for(let i=1;i<N;i++){
    dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + costs[i][0];
    dp[i][1] = Math.min(dp[i-1][2], dp[i-1][0]) + costs[i][1];
    dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + costs[i][2];
    }
    minCost = Math.min(minCost,...dp[N-1].filter((_,i) => i != c))
}
console.log(minCost)


