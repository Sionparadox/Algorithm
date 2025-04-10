const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
if (input.length === 0 || input[0] === '') {
    console.log(0);
    return;
}
const arr = input.map(v => v.split(' ').map(Number));

const graph = {};
for (let i=1; i<=arr.length+1;i++){
    graph[i] = [];
}
for (const [u, v, w] of arr){
    graph[u].push([v, w]);
    graph[v].push([u, w]);
}
let maxDist = 0;
let endNode = 1;
findEndNode(1, 0, new Set());
findEndNode(endNode, 0, new Set());
console.log(maxDist);
function findEndNode(node, k, visited){
    visited.add(node);
    if(k > maxDist){
        maxDist = k;
        endNode = node;
    }
    const next = graph[node];
    for (const [u, w] of next){
        if(!visited.has(u)){
            findEndNode(u, k+w, visited);
        }
    }
}
