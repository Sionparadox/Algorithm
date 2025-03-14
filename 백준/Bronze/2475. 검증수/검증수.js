const fs = require('fs');
const input = fs.readFileSync(0,'utf-8').toString().trim().split(' ').map(Number);
const ans = input.reduce((acc, v) => acc + v*v,0);
console.log(ans%10);
