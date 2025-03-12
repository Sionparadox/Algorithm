const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, R, Q] = input[0].split(' ').map(Number);
const arr = input.slice(1, N).map((item) => item.split(' ').map(Number));
const points = input.slice(N).map(Number);
const lines = Array(N + 1)
  .fill()
  .map(() => []);
for (const [p, q] of arr) {
  lines[p].push(q);
  lines[q].push(p);
}

const visited = Array(N + 1).fill(false);
const tree = Array(N + 1)
  .fill()
  .map(() => []);
const tree_size = Array(N + 1).fill(1);

make_tree(R);
cnt_subTree(R);
for (const v of points) {
  console.log(tree_size[v]);
}

function make_tree(node) {
  visited[node] = true;
  for (let i = 0; i < lines[node].length; i++) {
    const child = lines[node][i];
    if (!visited[child]) {
      tree[node].push(child);
      make_tree(child);
    }
  }
}

function cnt_subTree(node) {
  for (const n of tree[node]) {
    cnt_subTree(n);
    tree_size[node] += tree_size[n];
  }
}
