const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, W] = input[0].split(' ').map(Number);
const M = parseFloat(input[1]);
const pos = input.slice(2, 2 + N).map((v) => v.split(' ').map(Number));
const connected = input.slice(2 + N).map((v) => v.split(' ').map(Number));

const board = Array.from({ length: N + 1 }, () => Array(N + 1).fill(Infinity));
for (let i = 0; i < N - 1; i++) {
  for (let j = i; j < N; j++) {
    const dist = Math.sqrt(
      Math.pow(pos[i][0] - pos[j][0], 2) + Math.pow(pos[i][1] - pos[j][1], 2)
    );
    if (dist > M) continue;
    board[i + 1][j + 1] = dist;
    board[j + 1][i + 1] = dist;
  }
}
for (const [u, v] of connected) {
  board[u][v] = 0;
  board[v][u] = 0;
}

const dp = [...board[1]];

const visited = Array(N + 1).fill(false);
visited[1] = true;

while (true) {
  const idx = getMinimumIdx();
  if (idx == -1 || idx == N) break;
  visited[idx] = true;

  for (let i = 1; i < N + 1; i++) {
    if (visited[i]) continue;
    const temp = dp[idx] + board[idx][i];
    if (temp < dp[i]) {
      dp[i] = temp;
    }
  }
}

console.log(Math.floor(dp[N] * 1000));
function getMinimumIdx() {
  let min = Infinity;
  let idx = -1;
  for (let i = 1; i < N + 1; i++) {
    if (!visited[i] && dp[i] < min) {
      idx = i;
      min = dp[i];
    }
  }
  return idx;
}
