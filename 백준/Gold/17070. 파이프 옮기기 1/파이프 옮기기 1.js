const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [[N], ...home] = input.map(v => v.split(' ').map(Number));

// 0 1 2 : 가로 세로 대각
const dp = Array.from({length: N}, () => Array.from({length:N}, () => Array(3).fill(0)));
dp[0][1][0] = 1;

for (let r=0; r<N; r++){
    for (let c=0; c<N; c++){
        if(home[r][c] == 1) continue;
        if(c>1 && home[r][c-1] == 0) dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2];
        if(r>1 && home[r-1][c] == 0) dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2];
        if(c>0 && r>0 && home[r-1][c] == 0 && home[r][c-1] == 0 && home[r-1][c-1] == 0)
            dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2];
    }
}

console.log(dp[N-1][N-1].reduce((acc,v) => acc+v,0));