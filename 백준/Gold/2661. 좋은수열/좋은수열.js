const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();
// const input = fs.readFileSync('input.txt').toString().trim();
const N = +input;

backTrack([]);

function backTrack(arr) {
  if (arr.length == N) {
    console.log(arr.join(''));
    process.exit(0);
  }

  for (let i = 1; i < 4; i++) {
    arr.push(i);
    if (canMake(arr)) {
      backTrack(arr);
    }
    arr.pop();
  }
}

function canMake(seq) {
  const k = seq.length;
  for (let i = 1; i <= k / 2; i++) {
    const temp1 = seq.slice(k - i).join('');
    const temp2 = seq.slice(k - 2 * i, k - i).join('');
    if (temp1 === temp2) return false;
  }
  return true;
}
