const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [V,E] = input[0].split(' ').map(Number);
const arr = input.slice(1).map(item => item.split(' ').map(Number));
arr.sort((a,b) => a[2] - b[2]);

const parent = Array.from({length:V+1}, (_,i) => i);

let ans = 0;
for (const [u,v,w] of arr){
    if(find(u) != find(v)){
        union(u, v);
        ans += w;
    }
}
console.log(ans);

function find(node){
    if(parent[node] == node) return node;
    return parent[node] = find(parent[node]);
}

function union(u, v){
    const rootU = find(u);
    const rootV = find(v);
    if(rootU != rootV) parent[rootU] = rootV;
}