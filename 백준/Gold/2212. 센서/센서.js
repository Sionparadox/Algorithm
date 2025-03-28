const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = +input[0];
const K = +input[1];
const sensor = Array.from(new Set(input[2].split(' ').map(Number)));
sensor.sort((a, b) => a - b);
const diff = [];
for (let i = 0; i < sensor.length - 1; i++) {
  diff.push(sensor[i + 1] - sensor[i]);
}
diff.sort((a, b) => a - b);
let ans = 0;
for (let i = 0; i < diff.length - K + 1; i++) {
  ans += diff[i];
}
console.log(ans);
