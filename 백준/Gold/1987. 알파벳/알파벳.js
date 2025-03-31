const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [R, C] = input[0].split(' ').map(Number);
const board = input.slice(1).map((b) => b.split(''));

const visited = new Map();
for (let i = 'A'.charCodeAt(0); i <= 'Z'.charCodeAt(0); i++) {
  visited.set(String.fromCharCode(i), false);
}
visited.set(board[0][0], true);

const dr = [-1, 1, 0, 0];
const dc = [0, 0, -1, 1];
let ans = 0;
dfs(0, 0, 1);
console.log(ans);

function dfs(r, c, k) {
  for (let d = 0; d < 4; d++) {
    const newR = r + dr[d];
    const newC = c + dc[d];
    if (newR < 0 || newR >= R || newC < 0 || newC >= C) continue;
    if (visited.get(board[newR][newC])) continue;
    visited.set(board[newR][newC], true);
    dfs(newR, newC, k + 1);
    visited.set(board[newR][newC], false);
  }
  ans = Math.max(ans, k);
}
