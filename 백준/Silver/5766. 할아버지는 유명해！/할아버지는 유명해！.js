const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let idx = 0;
while (true) {
  const [N, M] = input[idx++].split(' ').map(Number);
  if (N == 0 && M == 0) break;
  const nums = input.slice(idx, idx + N).map((n) => n.split(' ').map(Number));
  idx += N;
  const players = Array(10001).fill(0);
  for (let i = 0; i < N; i++) {
    for (const n of nums[i]) {
      players[n] += 1;
    }
  }
  let value = Math.max(...players);
  value = Math.max(...players.filter((v) => v != 0 && v != value));
  console.log(
    players
      .map((v, i) => (v == value ? i : null))
      .filter((i) => i != null)
      .join(' ')
  );
}
