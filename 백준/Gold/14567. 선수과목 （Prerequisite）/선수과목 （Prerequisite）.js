const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);

const graph = Array.from({length:N+1}, () => []);
const degree = Array(N+1).fill(0);
const ans = Array(N+1).fill(1);

for (let i=1; i<=M; i++){
    const [s, e] = input[i].split(' ').map(Number);
    graph[s].push(e);
    degree[e]++;
}

const queue = [];
for(let i=1; i<=N; i++){
    if(degree[i] == 0) queue.push(i);
}

while(queue.length > 0){
    const node = queue.shift();
    for (const next of graph[node]){
        ans[next] = Math.max(ans[next], ans[node]+1);
        degree[next]--;
        if(degree[next] == 0) queue.push(next);
    }
}

console.log(ans.slice(1).join(' '));