const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();
// const input = fs.readFileSync('input.txt').toString().trim();

let str = input
  .replace(/<p>/gm, '\n')
  .replace(/<\/?[a-zA-Z]+ ?>/gm, '')
  .replace(/<div title="/gm, '\ntitle : ')
  .replace(/">/gm, '')
  .replace(/ +/gm, ' ');

console.log(
  str
    .split('\n')
    .map((s) => s.trim())
    .join('\n')
    .trim()
);
