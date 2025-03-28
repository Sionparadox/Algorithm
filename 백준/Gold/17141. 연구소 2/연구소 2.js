const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const room = input.slice(1).map((r) => r.split(' ').map(Number));

const virus = [];
let cleanSquare = 0;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (room[i][j] == 2) virus.push([i, j]);
    if (room[i][j] != 1) cleanSquare++;
  }
}
const combination = [];
makeCombine(0, []);
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
let ans = Infinity;
for (const pos of combination) {
  ans = Math.min(ans, bfs(pos));
}
console.log(ans == Infinity ? -1 : ans);

function bfs(selected) {
  const visited = Array.from({ length: N }, () => Array(N).fill(false));
  const queue = [];
  let cnt = cleanSquare - selected.length;
  for (const [i, j] of selected) {
    queue.push([i, j, 0]);
    visited[i][j] = true;
  }
  let idx = 0;
  let time = 0;
  while (idx < queue.length) {
    const [i, j, t] = queue[idx++];
    time = Math.max(time, t);
    if (time >= ans) return Infinity;
    for (let d = 0; d < 4; d++) {
      const newI = i + dx[d];
      const newJ = j + dy[d];
      if (
        newI >= 0 &&
        newI < N &&
        newJ >= 0 &&
        newJ < N &&
        !visited[newI][newJ] &&
        room[newI][newJ] != 1
      ) {
        visited[newI][newJ] = true;
        queue.push([newI, newJ, t + 1]);
        cnt--;
      }
    }
  }
  if (cnt != 0) return Infinity;
  return time;
}

function makeCombine(idx, arr) {
  if (arr.length == M) {
    combination.push([...arr]);
    return;
  }

  for (let i = idx; i < virus.length; i++) {
    makeCombine(i + 1, [...arr, virus[i]]);
  }
}
