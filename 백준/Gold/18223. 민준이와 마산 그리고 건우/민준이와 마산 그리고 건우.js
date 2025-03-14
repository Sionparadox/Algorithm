const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [V, E, P] = input[0].split(' ').map(Number);
const arr = input.slice(1, E + 1).map((item) => item.split(' ').map(Number));
const lines = Array(V + 1)
  .fill()
  .map(() => Array(V + 1).fill(Infinity));

for (let i = 0; i < E; i++) {
  const [a, b, c] = arr[i];
  lines[a][b] = c;
  lines[b][a] = c;
}

const dp1 = dijkstra(1);

const dp2 = dijkstra(P);
if (dp1[V] >= dp1[P] + dp2[V]) {
  console.log('SAVE HIM');
} else {
  console.log('GOOD BYE');
}

function dijkstra(s) {
  //초기화부분
  const dp = Array(V + 1).fill(Infinity);
  const visited = Array(V + 1).fill(false);
  for (let i = 1; i <= V; i++) {
    dp[i] = lines[s][i];
  }
  dp[s] = 0;
  visited[s] = true;

  for (let i = 0; i < V; i++) {
    //visited가 false인 idx중 dp[idx] 값이 가장 작은 idx를 찾기
    let minDist = Infinity;
    let idx = -1;
    for (let j = 1; j <= V; j++) {
      if (!visited[j] && dp[j] < minDist) {
        minDist = dp[j];
        idx = j;
      }
    }
    if(idx == -1) break;

    visited[idx] = true;
    for (let j = 1; j <= V; j++) {
      if (visited[j]) continue;
      dp[j] = Math.min(dp[j], dp[idx] + lines[idx][j]);
    }
  }
  return dp;
}
