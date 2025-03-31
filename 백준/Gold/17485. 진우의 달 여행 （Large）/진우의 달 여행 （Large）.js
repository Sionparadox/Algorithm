const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [[N, M], ...board] = input.map((b) => b.split(' ').map(Number));

const dp = Array.from({ length: N }, () =>
  Array.from({ length: M }, () => Array(3).fill(Infinity))
);

for (let i = 0; i < M; i++) {
  dp[0][i] = [board[0][i], board[0][i], board[0][i]];
}

for (let i = 1; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (j > 0) {
      dp[i][j][0] =
        Math.min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]) + board[i][j];
    }
    if (j < M - 1) {
      dp[i][j][2] =
        Math.min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1]) + board[i][j];
    }

    dp[i][j][1] = Math.min(dp[i - 1][j][0], dp[i - 1][j][2]) + board[i][j];
  }
}

let ans = Infinity;
for (let i = 0; i < M; i++) {
  ans = Math.min(ans, Math.min(...dp[N - 1][i]));
}
console.log(ans);
