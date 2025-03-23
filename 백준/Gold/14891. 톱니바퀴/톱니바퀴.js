const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const gear = input.slice(0, 4).map((s) => s.split('').map(Number));
const K = parseInt(input[4]);
const order = input.slice(5).map((s) => s.split(' ').map(Number));

//2번이 오른쪽, 6번이 왼쪽
const RIGHT = 2;
const LEFT = 6;

for (const [n, d] of order) {
  const curGear = n - 1;
  const directions = Array(4).fill(0);
  directions[curGear] = d;
  for (let i = curGear + 1; i < 4; i++) {
    if (gear[i][LEFT] != gear[i - 1][RIGHT]) {
      directions[i] = directions[i - 1] * -1;
    }
  }
  for (let i = curGear - 1; i > -1; i--) {
    if (gear[i][RIGHT] != gear[i + 1][LEFT]) {
      directions[i] = directions[i + 1] * -1;
    }
  }
  for (let i = 0; i < 4; i++) {
    rotate(i, directions[i]);
  }
}
console.log(gear.reduce((acc, v, i) => acc + v[0] * Math.pow(2, i), 0));

function rotate(idx, dir) {
  if (dir == 1) {
    gear[idx] = [gear[idx][7], ...gear[idx].slice(0, 7)];
  } else if (dir == -1) {
    gear[idx] = [...gear[idx].slice(1, 8), gear[idx][0]];
  }
}
