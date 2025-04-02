const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, K] = input[0].split(' ').map(Number);
const event = input.slice(1, 1 + K).map((e) => e.split(' ').map(Number));
const S = +input[1 + K];
const question = input.slice(2 + K).map((q) => q.split(' ').map(Number));

const graph = Array.from({ length: N + 1 }, () => Array(N + 1).fill(0));
for (const [u, v] of event) {
  graph[u][v] = -1;
  graph[v][u] = 1;
}

for (let k = 1; k <= N; k++) {
  for (let i = 1; i <= N; i++) {
    for (let j = 1; j <= N; j++) {
      if (graph[i][k] == 1 && graph[k][j] == 1) {
        graph[i][j] = 1;
        graph[j][i] = -1;
      }
    }
  }
}
for (const [u, v] of question) {
  console.log(graph[u][v]);
}

