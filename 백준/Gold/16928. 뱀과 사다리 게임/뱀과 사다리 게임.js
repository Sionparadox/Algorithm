const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const move = new Map(input.slice(1).map((item) => item.split(' ').map(Number)));
const visited = Array(101).fill(false);
const queue = [];
queue.push([1, 0]);
visited[1] = true;

while (queue.length > 0) {
  const [pos, cnt] = queue.shift();
  if (pos == 100) {
    console.log(cnt);
    break;
  }
  let normal = false;
  for (let i = 6; i > 0; i--) {
    let newPos = pos + i;
    if (newPos > 100) continue;
    if (move.has(newPos)) {
      newPos = move.get(newPos);
      if (!visited[newPos]) {
        queue.push([newPos, cnt + 1]);
        visited[newPos] = true;
      }
    } else if (!normal && !visited[newPos]) {
      normal = true;
      queue.push([newPos, cnt + 1]);
      visited[newPos] = true;
    }
  }
}
