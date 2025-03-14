const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [X, Y] = input[0].split(' ').map(Number);
const Z = Math.floor((Y * 100) / X);
let s = 1;
let e = 1000000000;
if (Z >= 99) {
  console.log(-1);
  process.exit(0);
}
while (s < e) {
  const mid = Math.floor((s + e) / 2);
  const rate = Math.floor(((Y + mid) * 100) / (X + mid));
  if (rate == Z) {
    s = mid + 1;
  } else {
    e = mid;
  }
}
console.log(s);
