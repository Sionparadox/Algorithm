const fs = require('fs');
const input = fs.readFileSync(0,'utf-8').toString().trim().split('\n');
const [N,M] = input[0].split(' ').map(Number);
const nums = Array.from(new Set(input[1].split(' ').map(Number)));
nums.sort((a,b) => a-b);

const ans = [];
dfs(0,0,'');
for (const s of ans){
    console.log(s.join(' '));
}

function dfs(k,idx, arr){
    if(k == M){
        ans.push(arr);
        return;
    }
    for (let i=idx;i<nums.length;i++){
        dfs(k+1,i,[...arr,nums[i]]);
    }
}