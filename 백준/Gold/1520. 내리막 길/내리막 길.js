const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [M, N] = input[0].split(' ').map(Number);
const board = input.slice(1).map((n) => n.split(' ').map(Number));

const dp = Array(M)
  .fill()
  .map(() => Array(N).fill(-1));

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

console.log(dfs(0, 0));

function dfs(i, j) {
  if (i == M - 1 && j == N - 1) return 1;
  if (dp[i][j] != -1) return dp[i][j];

  dp[i][j] = 0;

  for (let d = 0; d < 4; d++) {
    const x = i + dx[d];
    const y = j + dy[d];

    if (x >= 0 && x < M && y >= 0 && y < N) {
      if (board[i][j] > board[x][y]) {
        dp[i][j] += dfs(x, y);
      }
    }
  }

  return dp[i][j];
}
