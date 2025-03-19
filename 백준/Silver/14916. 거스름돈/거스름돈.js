const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = parseInt(input[0]);

let cnt = Math.floor(N / 5);
let coin = N % 5;
if (N == 1 || N == 3) {
  console.log(-1);
} else if (coin % 2 == 0) {
  console.log(cnt + Math.floor(coin / 2));
} else {
  console.log(cnt + Math.floor((coin + 5) / 2) - 1);
}
