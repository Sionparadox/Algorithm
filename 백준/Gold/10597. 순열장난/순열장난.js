const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();
// const input = fs.readFileSync('input.txt').toString().trim();

const nums = new Set();
const ans = [];
const max_N =
  input.length < 10 ? input.length : Math.floor((input.length - 9) / 2) + 9;
dfs(0);
console.log(ans.join(' '));

function dfs(k) {
  if (k == input.length) return true;

  for (let i = 1; i < 3; i++) {
    const n = parseInt(input.substring(k, k + i));
    if (n >= 1 && n <= max_N && !nums.has(n)) {
      nums.add(n);
      ans.push(n);
      if (dfs(k + i)) {
        return true;
      }

      nums.delete(n);
      ans.pop();
    }
  }
  return false;
}
