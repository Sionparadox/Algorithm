const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [[N, K], conveyor] = input.map((v) => v.split(' ').map(Number));

let idx = 0;
let step = 1;
const robot = Array(N).fill(false);

while (true) {
  rotate();

  move();

  if (conveyor[idx] > 0) {
    robot[0] = true;
    conveyor[idx] -= 1;
  }

  if (isFinish()) break;
  step++;
}
console.log(step);

function rotate() {
  idx = (idx - 1 + 2 * N) % (2 * N);
  for (let i = N - 1; i > 0; i--) {
    robot[i] = robot[i - 1];
  }
  robot[0] = false;
  robot[N - 1] = false;
}

function move() {
  for (let i = N - 2; i >= 0; i--) {
    if (robot[i] && !robot[i + 1] && conveyor[(idx + i + 1) % (2 * N)] > 0) {
      robot[i + 1] = true;
      robot[i] = false;
      conveyor[(idx + i + 1) % (2 * N)] -= 1;
    }
  }
  robot[N - 1] = false;
}

function isFinish() {
  cnt = 0;
  for (let i = 0; i < 2 * N; i++) {
    if (conveyor[i] == 0) cnt++;
  }
  return cnt >= K;
}
