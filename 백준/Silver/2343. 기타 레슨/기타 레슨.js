const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const weight = input[1].split(' ').map(Number);

let left = Math.max(...weight);
let right = weight.reduce((acc, v) => acc + v, 0);
let ans = right;

while (left <= right) {
  const mid = Math.floor((left + right) / 2);

  let cnt = 1;
  let subTotal = 0;
  for (const w of weight) {
    if (subTotal + w > mid) {
      cnt++;
      subTotal = w;
    } else {
      subTotal += w;
    }
  }

  if (cnt <= M) {
    ans = Math.min(ans, mid);
    right = mid - 1;
  } else {
    left = mid + 1;
  }
}
console.log(ans);
