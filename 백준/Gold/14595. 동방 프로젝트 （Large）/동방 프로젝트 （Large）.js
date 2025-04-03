const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [[N], [M], ...walls] = input.map((a) => a.split(' ').map(Number));

walls.sort((a, b) => a[0] - b[0]);

const broken = [];
for (let [x, y] of walls) {
  if (broken.length == 0 || broken.at(-1)[1] < x) {
    broken.push([x, y]);
  } else {
    broken.at(-1)[1] = Math.max(broken.at(-1)[1], y);
  }
}

let ans = N;
for (const [x, y] of broken) {
  ans -= y - x;
}
console.log(ans);
