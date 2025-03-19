const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const s1 = ['.', ...input[0].split('')];
const s2 = ['.', ...input[1].split('')];
const dp = Array(s1.length+1).fill().map(() => Array(s2.length+1).fill(0));

for(let i=1;i<s1.length;i++){
    for (let j=1;j<s2.length;j++){
        if(s1[i] == s2[j]) dp[i][j] = dp[i-1][j-1]+1;
        else {
            dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
        }
    }
}
const ans = dp[s1.length-1][s2.length-1]
const LCS = [];
let i=s1.length-1;
let j = s2.length-1;
while(LCS.length < ans){
    if(dp[i][j] == dp[i][j-1]){
        j--;
    } else if (dp[i][j] == dp[i-1][j]){
        i--;
    } else{
        LCS.push(s1[i]);
        i--;
        j--;
    }
}
console.log(ans);
console.log(LCS.reverse().join(''));