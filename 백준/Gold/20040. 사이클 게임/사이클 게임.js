const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const lines = input.slice(1).map((item) => item.split(' ').map(Number));
const parent = Array(N)
  .fill()
  .map((_, i) => i);

for (let i = 0; i < M; i++) {
  const [u, v] = lines[i];
  const rootU = find(u);
  const rootV = find(v);
  if (rootU == rootV) {
    console.log(i + 1);
    process.exit(0);
  }
  parent[rootV] = rootU;
}
console.log(0);

function find(v) {
  if (parent[v] == v) {
    return v;
  }
  return (parent[v] = find(parent[v]));
}
