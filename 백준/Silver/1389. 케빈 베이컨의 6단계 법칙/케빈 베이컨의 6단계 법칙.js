const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [[N, M], ...arr] = input.map((i) => i.split(' ').map(Number));

const distance = Array.from({ length: N + 1 }, () =>
  Array(N + 1).fill(Infinity)
);
for (let i = 0; i <= N; i++) {
  distance[i][i] = 0;
}

for (const [u, v] of arr) {
  distance[u][v] = 1;
  distance[v][u] = 1;
}

for (let k = 1; k <= N; k++) {
  for (let i = 1; i < N; i++) {
    for (let j = i + 1; j <= N; j++) {
      distance[i][j] = Math.min(
        distance[i][j],
        distance[i][k] + distance[k][j]
      );
      distance[j][i] = distance[i][j];
    }
  }
}
let min = Infinity;
let idx = -1;
for (let i = 1; i <= N; i++) {
  const sum = distance[i].slice(1).reduce((acc, v) => acc + v, 0);
  if (sum < min) {
    min = sum;
    idx = i;
  }
}
console.log(idx);
