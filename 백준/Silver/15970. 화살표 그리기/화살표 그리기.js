const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = parseInt(input[0]);
const arr = input.slice(1).map((str) => str.split(' ').map(Number).reverse());
arr.sort((a, b) => {
  if (a[0] == b[0]) {
    return a[1] - b[1];
  }
  return a[0] - b[0];
});

let color = arr[0][0] - 1;
let ans = 0;
for (let i = 0; i < N; i++) {
  if (arr[i][0] != color) {
    color = arr[i][0];
    ans += arr[i + 1][1] - arr[i][1];
  } else if (i == N - 1 || arr[i][0] != arr[i + 1][0]) {
    ans += arr[i][1] - arr[i - 1][1];
  } else {
    ans += Math.min(arr[i + 1][1] - arr[i][1], arr[i][1] - arr[i - 1][1]);
  }
}
console.log(ans);
