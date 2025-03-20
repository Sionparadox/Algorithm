const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = parseInt(input[0]);

const tree = Array(N + 1)
  .fill()
  .map(() => ({ left: -1, right: -1 }));
for (let i = 1; i <= N; i++) {
  const [left, right] = input[i].split(' ').map(Number);
  tree[i].left = left;
  tree[i].right = right;
}
let K = BigInt(input[N + 1]);

console.log(dfs(1, K));
function dfs(node, k) {
  if (tree[node].left == -1 && tree[node].right == -1) {
    return node;
  } else if (tree[node].left == -1) {
    return dfs(tree[node].right, k);
  } else if (tree[node].right == -1) {
    return dfs(tree[node].left, k);
  } else {
    return dfs(
      k % 2n == 0n ? tree[node].right : tree[node].left,
      BigInt(k / 2n) + (k % 2n)
    );
  }
}
