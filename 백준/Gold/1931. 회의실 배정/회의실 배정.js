const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = parseInt(input[0]);
const schedule = input.slice(1).map((str) => str.split(' ').map(Number));
schedule.sort((a, b) => {
  if (a[1] == b[1]) {
    return a[0] - b[0];
  }
  return a[1] - b[1];
});

let e = 0;
let ans = 0;
for (let i = 0; i < N; i++) {
  if (schedule[i][0] >= e) {
    ans++;
    e = schedule[i][1];
  }
}
console.log(ans);
