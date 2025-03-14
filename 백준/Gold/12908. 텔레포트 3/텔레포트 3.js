const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const nodes = input.slice(0, 2).map((item) => item.split(' ').map(Number));
input.slice(2).map((item) => {
  const arr = item.split(' ').map(Number);
  nodes.push(arr.slice(0, 2));
  nodes.push(arr.slice(2));
});

const lines = Array(8)
  .fill()
  .map(() => Array(8).fill(Infinity));
for (let i = 0; i < 8; i++) {
  for (let j = 0; j < 8; j++) {
    if (i == j) {
      lines[i][j] = 0;
      continue;
    }

    const d =
      Math.abs(nodes[i][0] - nodes[j][0]) + Math.abs(nodes[i][1] - nodes[j][1]);
    lines[i][j] = d;
    if (
      Math.floor(i / 2) == Math.floor(j / 2) &&
      Math.abs(i - j) == 1 &&
      i > 1
    ) {
      lines[i][j] = Math.min(lines[i][j], 10);
    }
  }
}

visited = Array(8).fill(false);
dp = [...lines[0]];
visited[0] = true;
for (let i = 0; i < 8; i++) {
  let minDist = Infinity;
  let idx = -1;
  for (let j = 0; j < 8; j++) {
    if (!visited[j] && dp[j] < minDist) {
      minDist = dp[j];
      idx = j;
    }
  }
  if (idx == 1) {
    break;
  } else if (idx == -1) {
    break;
  }

  visited[idx] = true;
  for (let j = 1; j < 8; j++) {
    if (visited[j]) continue;
    dp[j] = Math.min(dp[j], dp[idx] + lines[idx][j]);
  }
}

console.log(dp[1]);
