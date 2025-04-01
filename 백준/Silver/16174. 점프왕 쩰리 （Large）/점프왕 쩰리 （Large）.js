const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = +input[0];
const board = input.slice(1).map((b) => b.split(' ').map(Number));
const canMove = Array.from({ length: N }, () => Array(N).fill(false));
canMove[N - 1][N - 1] = true;

for (let i = N - 1; i >= 0; i--) {
  for (let j = N - 1; j >= 0; j--) {
    if (i == N - 1 && j == N - 1) continue;
    const newR = i + board[i][j];
    const newC = j + board[i][j];
    if ((newR < N && canMove[newR][j]) || (newC < N && canMove[i][newC])) {
      canMove[i][j] = true;
    }
  }
}

console.log(canMove[0][0] ? 'HaruHaru' : 'Hing');
