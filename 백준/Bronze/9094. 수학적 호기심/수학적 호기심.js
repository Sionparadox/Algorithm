const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, ...num] = input.map((n) => n.split(' ').map(Number));

for (const [n, m] of num) {
  console.log(check(n, m));
}

function check(n, m) {
  let ans = 0;
  for (let i = 1; i < n - 1; i++) {
    for (let j = i + 1; j < n; j++) {
      if ((i * i + j * j + m) % (i * j) == 0) {
        ans++;
      }
    }
  }
  return ans;
}
