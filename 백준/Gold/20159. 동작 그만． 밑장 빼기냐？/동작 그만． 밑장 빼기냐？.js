const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = +input[0];
const card = input[1].split(' ').map(Number);
const prefixOdd = [card[0]];
const prefixEven = [card[1]];

for (let i = 2; i < N; i += 2) {
  prefixOdd.push(prefixOdd.at(-1) + card[i]);
  prefixEven.push(prefixEven.at(-1) + card[i + 1]);
}

let ans = Math.max(prefixOdd[N / 2 - 1], prefixEven[N / 2 - 1]);

for (let i = 0; i < N; i += 2) {
  let oddSum = prefixOdd[i / 2];

  let evenSum1 = prefixEven[N / 2 - 1] - prefixEven[i / 2];
  let evenSum2 =
    prefixEven[N / 2 - 1] - prefixEven[i / 2] - card[N - 1] + card[i + 1];

  ans = Math.max(ans, oddSum + evenSum1, oddSum + evenSum2);
}
console.log(ans);
