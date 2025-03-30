const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = +input[0];
const town = input.slice(1).map((t) => t.split(' ').map(Number));
town.sort((a, b) => a[0] - b[0]);

let total = town.reduce((acc, v) => acc + v[1], 0);
let sum = 0;
for (const [d, w] of town) {
  sum += w;
  if (sum >= total / 2) {
    console.log(d);
    break;
  }
}
