const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = +input[0];
const K = +input[1];
const apple = input.slice(2, 2 + K).map((v) => v.split(' ').map(Number));
const L = input[2 + K];
const dir = input.slice(3 + K).map((v) => {
  const [x, c] = v.split(' ');
  return [+x, c];
});

const board = Array.from(
  { length: N + 1 },
  () => Array.from({ length: N + 1 }),
  () => ''
);
for (let [x, y] of apple) {
  board[x][y] = 'a';
}

const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];

let dirIdx = 0;
let currDir = 0;
let time = 1;
const dequeue = [[1, 1]];
while (true) {
  const [r, c] = dequeue[0];
  const [nr, nc] = [r + dx[currDir], c + dy[currDir]];
  if (nr < 1 || nr > N || nc < 1 || nc > N) break;
  if (board[nr][nc] == 's') break;

  dequeue.unshift([nr, nc]);
  if (board[nr][nc] != 'a') {
    const [tailR, tailC] = dequeue.pop();
    board[tailR][tailC] = '';
  } else {
  }
  board[nr][nc] = 's';
  if (dirIdx < dir.length && time == dir[dirIdx][0]) {
    const d = dir[dirIdx][1];
    if (d == 'D') {
      currDir = (currDir + 1) % 4;
    } else {
      currDir = (currDir + 3) % 4;
    }
    dirIdx++;
  }
  time++;
}
console.log(time);
