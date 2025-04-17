const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const K = +input[0];
const arr = input[1].split(' ').map(Number);
const S = arr.reduce((acc, v) => acc+v, 0);

const check = Array(S+1).fill(false);

dfs(0, 0, 0);
let cnt = 0;
for (const b of check){
    if(!b) cnt++;
}
console.log(cnt);

function dfs(k, left, right){
    if(k == K){
        check[Math.abs(left - right)] = true;
        return;
    }
    
    dfs(k+1, left+arr[k], right);
    
    dfs(k+1, left, right+arr[k]);
    
    dfs(k+1, left, right);
}
