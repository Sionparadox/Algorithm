const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const pos = input.slice(1, 1 + N).map((p) => p.split(' ').map(Number));
const relate = input.slice(1 + N).map((r) => r.split(' ').map(Number));

const parent = Array.from({ length: N + 1 }, (_, i) => i);

for (const [u, v] of relate) {
  union(u, v);
}
const distance = [];
for (let i = 0; i < N - 1; i++) {
  for (let j = i + 1; j < N; j++) {
    const d = Math.sqrt(
      Math.pow(pos[i][0] - pos[j][0], 2) + Math.pow(pos[i][1] - pos[j][1], 2)
    );
    distance.push([i + 1, j + 1, d]);
  }
}
distance.sort((a, b) => a[2] - b[2]);

let ans = 0;
for (const [u, v, d] of distance) {
  if (union(u, v)) {
    ans += d;
  }
}
console.log(ans.toFixed(2));

function find(node) {
  if (parent[node] == node) return node;
  return (parent[node] = find(parent[node]));
}

function union(u, v) {
  const rootU = find(u);
  const rootV = find(v);
  if (rootU != rootV) {
    parent[rootV] = find(rootU);
    return true;
  }
  return false;
}
