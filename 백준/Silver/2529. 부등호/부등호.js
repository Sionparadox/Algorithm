const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const k = +input[0];
const sign = input[1].split(' ');
const visited = Array(10).fill(false);

const ans = [];

backTrack(0, []);
console.log(ans.at(-1));
console.log(ans[0]);

function backTrack(n, arr) {
  if (arr.length == k + 1) {
    ans.push(arr.join(''));
    return;
  }

  for (let i = 0; i < 10; i++) {
    if (!visited[i]) {
      if (
        arr.length == 0 ||
        (sign[n - 1] == '<' && arr.at(-1) < i) ||
        (sign[n - 1] == '>' && arr.at(-1) > i)
      ) {
        visited[i] = true;
        backTrack(n + 1, [...arr, i]);
        visited[i] = false;
      }
    }
  }
}
