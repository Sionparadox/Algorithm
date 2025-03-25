const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();
// const input = fs.readFileSync('input.txt').toString().trim();
const N = parseInt(input);

const output = Array(N)
  .fill()
  .map(() => Array(N * 2 - 1).fill(' '));

draw(0, N - 1, N);
console.log(output.map((o) => o.join('')).join('\n'));

function draw(x, y, k) {
  if (k == 3) {
    output[x][y] = '*';
    output[x + 1][y - 1] = '*';
    output[x + 1][y + 1] = '*';
    output[x + 2].splice(y - 2, 5, '*', '*', '*', '*', '*');
    return;
  }
  const size = parseInt(k / 2);
  draw(x, y, size);
  draw(x + size, y + size, size);
  draw(x + size, y - size, size);
}
