const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [[N], [M], ...arr] = input.map(v => v.split(' ').map(Number));

const graph = Array.from({length:N}, () => Array(N).fill(Infinity));
for (let i=0; i<N; i++){
    graph[i][i] = 0;
}
for (const [u, v, w] of arr){
    graph[u-1][v-1] = Math.min(graph[u-1][v-1], w);
}

for (let k=0; k<N; k++){
    for (let i=0; i<N; i++){
        for (let j=0; j<N; j++){
            graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
        }
    }
}

console.log(graph.map(g => g.map(x => x == Infinity ? 0 : x).join(' ')).join('\n'));
