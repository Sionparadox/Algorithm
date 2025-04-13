const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = +input[0];
const M = +input[1];
const arr = input.slice(2,M+2).map(v => v.split(' ').map(Number));
const [S, E] = input[M+2].split(' ').map(Number);

const graph = Array.from({length: N+1}, () => Array(N+1).fill(Infinity));
const visited = Array(N+1).fill(false);
const dp = Array(N+1).fill(Infinity);

for (let i=1; i<=N; i++){
    graph[i][i] = 0;
}
for (const [u, v, w] of arr){
    graph[u][v] = Math.min(graph[u][v], w)
}

dijkstra(S);
console.log(dp[E]);

function dijkstra(node){
    dp[node] = 0;
    
    for (let i=1; i<=N; i++){
        let minVal = Infinity;
        let idx = -1;
        for (let j=1; j<=N; j++){
            if(!visited[j] && dp[j] < minVal){
                minVal = dp[j];
                idx = j;
            }
        }
        
        if(idx == -1) break;
        visited[idx] = true;
        
        for (let k=1; k<=N; k++){
            if(!visited[k] && dp[k] > dp[idx] + graph[idx][k]){
                dp[k] = dp[idx] + graph[idx][k];
            }
        }
    }
}