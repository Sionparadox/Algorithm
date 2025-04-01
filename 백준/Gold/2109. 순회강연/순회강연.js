const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = +input[0];
const arr = input.slice(1).map((a) => a.split(' ').map(Number));

arr.sort((a, b) => {
  if (a[1] == b[1]) return a[0] - b[0];
  return a[1] - b[1];
});

let ans = 0;
while (arr.length != 0) {
  const temp = [];
  const [p, d] = arr.pop();
  temp.push([p, d]);
  while (arr.length != 0 && arr.at(-1)[1] == d) {
    temp.push(arr.pop());
  }
  temp.sort((a, b) => a[0] - b[0]);
  ans += temp.pop()[0];
  if (d == 1) break;
  temp.forEach((pd) => arr.push([pd[0], pd[1] - 1]));
}
console.log(ans);
