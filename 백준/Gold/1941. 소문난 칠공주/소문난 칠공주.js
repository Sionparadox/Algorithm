const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const seat = input.map((s) => s.split(''));

const group = [];
makeCombine(0, []);
let ans = 0;
const dir = [
  [0, -1],
  [0, 1],
  [-1, 0],
  [1, 0],
];
for (const g of group) {
  const pos = [];
  let cnt = 0;
  for (let p of g) {
    const row = Math.floor(p / 5);
    const col = p % 5;
    pos.push([row, col]);
    if (seat[row][col] == 'S') cnt++;
  }
  if (cnt < 4) continue;

  const visited = new Set();
  const queue = [];
  queue.push(pos[0]);
  visited.add(`${pos[0][0]} ${pos[0][1]}`);

  while (queue.length > 0) {
    const [x, y] = queue.shift();
    for (const [dx, dy] of dir) {
      const newX = x + dx;
      const newY = y + dy;
      const index = pos.findIndex((item) => item[0] == newX && item[1] == newY);
      const str = `${newX} ${newY}`;
      if (index != -1 && !visited.has(str)) {
        visited.add(str);
        queue.push([newX, newY]);
      }
    }
  }
  if (visited.size == 7) ans++;
}

console.log(ans);

function makeCombine(idx, arr) {
  if (arr.length == 7) {
    group.push([...arr]);
    return;
  }

  for (let i = idx; i < 25; i++) {
    arr.push(i);
    makeCombine(i + 1, arr);
    arr.pop();
  }
}
