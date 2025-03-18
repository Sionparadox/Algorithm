const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [V,E] = input[0].split(' ').map(Number);
const lines = input.slice(1).map(line => line.split(' ').map(Number));
lines.sort((a,b) => a[2] - b[2]);
const parent = Array(V+1).fill().map((_,i)=>i);

let mstWeight = 0;
for (const [u,v,w] of lines){
    if(find(u) != find(v)){
        union(u,v);
        mstWeight += w;
    }
}
console.log(mstWeight);

function find(node){
    if(parent[node] == node) return node;
    return parent[node] = find(parent[node]);
}

function union(u,v){
    const rootU = find(u);
    const rootV = find(v);
    if(rootU != rootV){
        parent[rootU] = rootV;
    }
}