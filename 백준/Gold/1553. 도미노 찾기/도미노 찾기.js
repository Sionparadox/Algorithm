const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const board = input.map((s) => s.split('').map(Number));
const visited = Array(7)
  .fill()
  .map(() => Array(7).fill(false));

console.log(backTrack(0, 0));

function backTrack(row, col) {
  if (row >= 8) return 1;

  let nextRow = row;
  let nextCol = col + 1;
  if (nextCol >= 7) {
    nextRow = row + 1;
    nextCol = 0;
  }

  if (board[row][col] == -1) {
    return backTrack(nextRow, nextCol);
  }

  let cnt = 0;
  if (col < 6 && board[row][col + 1] != -1) {
    const x = board[row][col];
    const y = board[row][col + 1];
    if (!visited[x][y] && !visited[y][x]) {
      visited[x][y] = true;
      visited[y][x] = true;
      board[row][col] = -1;
      board[row][col + 1] = -1;

      cnt += backTrack(nextRow, nextCol);

      visited[x][y] = false;
      visited[y][x] = false;
      board[row][col] = x;
      board[row][col + 1] = y;
    }
  }

  if (row < 7 && board[row + 1][col] != -1) {
    const x = board[row][col];
    const y = board[row + 1][col];
    if (!visited[x][y] && !visited[y][x]) {
      visited[x][y] = true;
      visited[y][x] = true;
      board[row][col] = -1;
      board[row + 1][col] = -1;

      cnt += backTrack(nextRow, nextCol);

      visited[x][y] = false;
      visited[y][x] = false;
      board[row][col] = x;
      board[row + 1][col] = y;
    }
  }

  return cnt;
}
