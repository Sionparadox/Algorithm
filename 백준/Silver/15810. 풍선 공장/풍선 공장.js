const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, M] = input[0].split(' ');
const times = input[1].split(' ').map(Number);

let left = 1;
let right = Math.min(...times) * M;

while (left < right) {
  const mid = Math.floor((left + right) / 2);
  const balloon = times.reduce((acc, i) => acc + Math.floor(mid / i), 0);
  if (balloon >= M) right = mid;
  else left = mid + 1;
}
console.log(left);
