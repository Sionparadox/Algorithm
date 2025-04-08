const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [[N, M], arr] = input.map(v => v.split(' ').map(Number));

const notUse = new Set(arr);
const dp = Array.from({length:N+1}, () => Array(42).fill(Infinity));
dp[0][0] = 0;

for (let i=0; i<N; i++){
    for (let j=0; j<40; j++){
        if(dp[i][j] == Infinity) continue;
        
        if(notUse.has(i+1)){
            dp[i+1][j] = Math.min(dp[i+1][j], dp[i][j]);
        }
        if(j >= 3){
            dp[i+1][j-3] = Math.min(dp[i][j], dp[i+1][j-3])
        }
        
        dp[i+1][j] = Math.min(dp[i+1][j], dp[i][j] + 10000);
        
        for (let k=1; k<=3; k++){
            if(i + k > N) break;
            dp[i+k][j+1] = Math.min(dp[i+k][j+1], dp[i][j]+25000);
        }
        
        for (let k=1; k<=5; k++){
            if(i + k > N) break;
            dp[i+k][j+2] = Math.min(dp[i+k][j+2], dp[i][j]+37000);
        }
    }
}
console.log(Math.min(...dp[N]));