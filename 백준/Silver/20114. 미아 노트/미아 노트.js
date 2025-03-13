const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const [N, H, W] = input[0].split(' ').map(Number);
const str = input.slice(1);
const ans = Array(N).fill('?');
for (let h = 0; h < H; h++) {
  for (let w = 0; w < N * W; w++) {
    ans[Math.floor(w / W)] =
      str[h][w] != '?' ? str[h][w] : ans[Math.floor(w / W)];
  }
}
console.log(ans.join(''));
