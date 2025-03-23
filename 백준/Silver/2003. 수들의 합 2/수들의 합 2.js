const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);

let ans = 0;
let s = 0;
let e = 0;
let sum = 0;
while (s <= e && e <= N) {
  if (sum > M) {
    sum -= arr[s++];
  } else if (sum < M) {
    sum += arr[e++];
  } else {
    ans++;
    s++;
    e = s;
    sum = 0;
  }
}
console.log(ans);
