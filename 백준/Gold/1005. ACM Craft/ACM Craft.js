const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const T = parseInt(input[0]);

let line = 1;
for (let t=0;t<T;t++){
    const [N,K] = input[line++].split(' ').map(Number);
    const times = input[line++].split(' ').map(Number);
    const arr = input.slice(line, line+K).map(v=>v.split(' ').map(Number));
    const W = parseInt(input[line+K]);
    line += K+1;
    const tree = Array(N+1).fill().map(()=>[]);
    const degree = Array(N+1).fill(0);
    for(const [s,e] of arr){
        tree[s].push(e);
        degree[e]++;
    }
    
    const dp = Array(N+1).fill(0);
    const queue = [];
    for(let i=1;i<=N;i++){
        if(degree[i] == 0){
            queue.push(i);
            dp[i] = times[i-1];
        }
    }
    
    while(queue.length != 0){
        const now = queue.shift();
        for(const next of tree[now]){
            dp[next] = Math.max(dp[next], dp[now] + times[next-1]);
            degree[next]--;
            if(degree[next] == 0){
                queue.push(next);
            }
        }
    }
    console.log(dp[W]);
}