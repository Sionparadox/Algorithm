const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [[N, M], ...road] = input.map((r) => r.split(' ').map(Number));

const parent = Array.from({ length: N + 1 }, (_, i) => i);
road.sort((a, b) => a[2] - b[2]);

let dist = 0;
let sum = 0;
for (const [a, b, c] of road) {
  sum += c;
  if (union(a, b)) {
    dist += c;
  }
}

const set = new Set();
for (let i = 1; i <= N; i++) {
  set.add(find(i));
}
if (set.size != 1) {
  console.log(-1);
} else {
  console.log(sum - dist);
}

function find(node) {
  if (parent[node] == node) return node;
  return (parent[node] = find(parent[node]));
}

function union(u, v) {
  const rootU = find(u);
  const rootV = find(v);
  if (rootU != rootV) {
    parent[rootV] = rootU;
    return true;
  }
  return false;
}
