const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split(' ');
const arr = input.slice(0,-1).map(Number);
const len = arr.length;
const dp = Array.from({length: len+1}, () => Array.from({length:5}, () => Array(5).fill(Infinity)));

dp[0][0][0] = 0;

for (let i=0; i<len; i++){
    const cmd = arr[i];
    for (let l=0; l<5; l++){
        for (let r=0; r<5; r++){
            dp[i+1][l][cmd] = Math.min(dp[i+1][l][cmd], dp[i][l][r] + power(r,cmd))
            dp[i+1][cmd][r] = Math.min(dp[i+1][cmd][r], dp[i][l][r] + power(l,cmd))
        }
    }
}
console.log(Math.min(...dp[len].map(d => Math.min(...d))));

function power(s,e){
    if(s == 0) return 2;
    if(s == e) return 1;
    if(Math.abs(s-e) == 2) return 4;
    return 3;
}