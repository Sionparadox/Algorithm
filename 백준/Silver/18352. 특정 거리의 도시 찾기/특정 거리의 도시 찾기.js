const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, M, K, X] = input[0].split(' ').map(Number);
const arr = input.slice(1).map((item) => item.split(' ').map(Number));
const lines = Array(N + 1)
  .fill()
  .map(() => []);
for (const [s, e] of arr) {
  lines[s].push(e);
}

const visited = Array(N + 1).fill(-1);
visited[X] = 0;
const queue = [X];
let idx = 0;

while (idx < queue.length) {
  const node = queue[idx++];
  if (visited[node] > K) continue;

  for (const v of lines[node]) {
    if (visited[v] == -1) {
      visited[v] = visited[node] + 1;
      queue.push(v);
    }
  }
}

const res = visited.map((v, i) => (v == K ? i : -1)).filter((v) => v != -1);
if (res.length == 0) {
  console.log(-1);
} else {
  res.sort((a, b) => a > b);
  console.log(res.join('\n'));
}
