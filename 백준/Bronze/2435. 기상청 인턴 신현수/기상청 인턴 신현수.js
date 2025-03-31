const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [[N, K], nums] = input.map((n) => n.split(' ').map(Number));

let sum = nums.slice(0, K).reduce((acc, v) => acc + v, 0);

let ans = sum;
for (let i = K; i < N; i++) {
  sum += nums[i] - nums[i - K];
  ans = Math.max(ans, sum);
}
console.log(ans);
