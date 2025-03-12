const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = parseInt(input[0]);
const arr = input.slice(1).map((item) => item.split(' ').map(Number));
const points = [];
for (let i = 0; i < N; i++) {
  const [x, r] = arr[i];
  points.push({ pos: x - r, type: 's', idx: i });
  points.push({ pos: x + r, type: 'e', idx: i });
}
points.sort((a, b) => {
  if (a.pos != b.pos) return a.pos - b.pos;
  return a.type == 'e' ? 1 : -1;
});

const stack = [];
let ans = 'YES';
for (const p of points) {
  if (p.type == 's') {
    stack.push(p.idx);
  } else {
    if (stack.at(-1) == p.idx) {
      stack.pop();
    } else {
      ans = 'NO';
      break;
    }
  }
}
console.log(ans);
