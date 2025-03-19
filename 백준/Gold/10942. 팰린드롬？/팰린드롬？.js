const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = parseInt(input[0]);
const nums = [0,...input[1].split(' ').map(Number)];
const M = parseInt(input[2]);
const questions = input.slice(3).map(q => q.split(' ').map(Number));

const dp = Array(N+1).fill().map(()=>Array(N+1).fill(false));
for (let i=1;i<=N;i++){
    dp[i][i] = true;
    if(i<N && nums[i] == nums[i+1]) dp[i][i+1] = true;
}

for (let l=3;l<=N;l++){
    for(let i=1;i<=N-l+1;i++){
        const j = i + l - 1;
        if(nums[i] == nums[j] && dp[i+1][j-1]){
            dp[i][j] = true;
        }
    }
}

let ans = '';
for (const [s,e] of questions){
    ans += (dp[s][e] ? 1 : 0) + '\n';
}
console.log(ans.trim());