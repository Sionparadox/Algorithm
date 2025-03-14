const fs = require('fs');
const input = fs.readFileSync(0,'utf-8').toString().trim().split('\n');
const [N,M] = input[0].split(' ').map(Number);
const nums = input[1].split(' ').map(Number).sort((a,b)=> a-b);

const visited = Array(N).fill(false);
const S = new Set();

dfs(0,[]);
for (const s of S.values()){
    console.log(s);
}

function dfs(k,arr){
    if(k==M) {
        S.add(arr.join(' '));
        return;
    }
    for (let i=0;i<N;i++){
        if(!visited[i]){
            visited[i] = true;
            dfs(k+1,[...arr,nums[i]]);
            visited[i] = false;
        }
    }
}