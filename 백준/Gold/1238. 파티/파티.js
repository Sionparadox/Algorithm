const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [[N, M, X], ...arr] = input.map(v => v.split(' ').map(Number));

const graph = Array.from({length:N+1}, () => []);
const graph2 = Array.from({length:N+1}, () => []);

for (const [s, e, t] of arr){
    graph[s].push([e, t]);
    graph2[e].push([s, t]);
}

const res1 = dijkstra(X, graph);
const res2 = dijkstra(X, graph2);
let ans = 0;
for (let i=1; i<=N; i++){
    ans = Math.max(ans, res1[i] + res2[i]);
}
console.log(ans);

function dijkstra(s, arr){
    const dist = Array(N+1).fill(Infinity);
    const visited = Array(N+1).fill(false);
    dist[s] = 0;
    const queue = [[0, s]];
    while(queue.length > 0){
        queue.sort((a,b) => a[0] - b[0]);
        const [d, node] = queue.shift();
        if(visited[node]) continue;
        
        visited[node] = true;
        for (const [v, w] of arr[node]){
            if(d+w < dist[v]){
                dist[v] = d + w;
                queue.push([dist[v], v]);
            }
        }
    }
    return dist;
}