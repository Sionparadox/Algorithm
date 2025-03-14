const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
let t = 0;
while (true) {
  const [n, k] = input[t++].split(' ').map(Number);
  if (n == 0 && k == 0) break;
  const arr = input[t++].split(' ').map(Number);

  if (n == 1) {
    console.log(0);
    continue;
  }

  const parent = Array(n).fill(-1);

  let parentIdx = -1;
  for (let i = 1; i < n; i++) {
    if (arr[i] != arr[i - 1] + 1) {
      parentIdx++;
    }
    parent[i] = parentIdx;
  }

  let kIdx = -1;
  for (let i = 0; i < n; i++) {
    if (arr[i] == k) kIdx = i;
  }
  const kParent = parent[kIdx];
  if (kParent == -1) {
    console.log(0);
    continue;
  }
  const kGrandP = parent[kParent];
  if (kGrandP == -1) {
    console.log(0);
    continue;
  }

  let ans = 0;
  for (let i = 0; i < n; i++) {
    const p = parent[i];
    if (p != kParent && parent[p] == kGrandP) {
      ans++;
    }
  }
  console.log(ans);
}
