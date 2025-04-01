const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim();
const N = +input;

let num = 666;
let cnt = 0;
while (cnt < N) {
  if (isDevilNum(num)) cnt++;
  num++;
}

console.log(num - 1);
function isDevilNum(n) {
  let cnt = 0;
  while (n > 0) {
    if (n % 10 == 6) {
      cnt++;
      if (cnt == 3) break;
    } else {
      cnt = 0;
    }
    n = Math.floor(n / 10);
  }

  if (cnt >= 3) return true;
  return false;
}
