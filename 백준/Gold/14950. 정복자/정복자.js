const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, M, t] = input[0].split(' ').map(Number);
const lines = input.slice(1).map((v) => v.split(' ').map(Number));
lines.sort((a, b) => a[2] - b[2]);

const parent = Array(N + 1)
  .fill()
  .map((_, i) => i);

let mst = 0;
for (const [u, v, w] of lines) {
  if (find(u) != find(v)) {
    union(u, v);
    mst += w;
  }
}
mst += Math.floor((t * (N - 1) * (N - 2)) / 2);
console.log(mst);

function find(node) {
  if (parent[node] == node) return node;
  return (parent[node] = find(parent[node]));
}

function union(u, v) {
  const rootU = find(u);
  const rootV = find(v);
  if (rootU != rootV) parent[rootU] = find(rootV);
}
