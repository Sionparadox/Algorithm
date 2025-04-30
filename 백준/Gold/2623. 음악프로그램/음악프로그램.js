const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [[N, M], ...arr] = input.map(v => v.split(' ').map(Number));

const degree = Array(N+1).fill(0);
const graph = Array.from({length:N+1}, () => []);
for (const order of arr){
    for (let i=1; i<order[0]; i++){
        degree[order[i+1]]++;
        graph[order[i]].push(order[i+1]);
    }
}

const ans = [];
const queue = [];

for (let i=1; i<N+1; i++){
    if(degree[i] == 0) queue.push(i);
}

while (queue.length > 0){
    const now = queue.shift();
    ans.push(now);
    for (const next of graph[now]){
        degree[next]--;
        if(degree[next] == 0) queue.push(next);
    }
}
if(ans.length != N) console.log(0);
else console.log(ans.join('\n'));