const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = +input[0];
const arr = input.slice(1, N+1).map(v => v.split(' is ').map(s => s.charCodeAt(0)-97));
const M = +input[N+1];
const que = input.slice(N+2).map(v => v.split(' is ').map(s => s.charCodeAt(0)-97));

const graph = Array.from({length:26}, () => Array(26).fill(false));
for (const [s,e] of arr){
    graph[s][e] = true;
}

for (let k=0; k<26; k++){
    for (let i=0; i<26; i++){
        for (let j=0; j<26; j++){
            graph[i][j] = graph[i][j] || (graph[i][k] && graph[k][j]);
        }
    }
}

for (const [s,e] of que){
    console.log(graph[s][e] ? 'T': 'F');
}