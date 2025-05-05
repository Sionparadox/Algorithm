const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const [T, ...arr] = input[1].split(' ').map(Number);
const party = input.slice(2).map(v => v.split(' ').map(Number).slice(1));

const parent = Array.from({length:N+1}, (_,i) => i);

for (const p of party){
    for (let i=1; i<p.length; i++){
        union(p[0], p[i]);
    }
}

const truth = new Set(arr.map(find));
let ans = 0;

for (const p of party){
    let flag = true;
    for (let i=0; i<p.length; i++){
        if(truth.has(find(p[i]))) flag = false;
    }
    if(flag) ans++;
}
console.log(ans);



function find(node){
    if(node == parent[node]) return node;
    return parent[node] = find(parent[node]);
}

function union(u, v){
    const rootU = find(u);
    const rootV = find(v);
    if(rootU != rootV) parent[rootV] = rootU;
}