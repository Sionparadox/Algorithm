const fs = require('fs');
const { exit } = require('process');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, K] = input[0].split(' ').map(Number);
const arr = Array(N + 1).fill(true);
let cnt = 0;
for (let i = 2; i <= N; i++) {
  if (arr[i]) {
    for (let j = i; j <= N; j += i) {
      if (arr[j]) {
        cnt++;
        arr[j] = false;
      }
      if (cnt == K) {
        console.log(j);
        exit(0);
      }
    }
  }
}
