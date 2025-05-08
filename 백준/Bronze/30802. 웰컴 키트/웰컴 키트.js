const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = +input[0];
const size = input[1].split(' ').map(Number);
const [T, P] = input[2].split(' ').map(Number);
console.log(size.reduce((acc, v) => acc+Math.ceil(v/T), 0));
console.log(Math.floor(N/P), N%P);