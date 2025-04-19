const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = +input[0];
const arr = input[1].split(' ').map(Number);
const x = +input[2];

const set = new Set();
let ans = 0;
for (const n of arr){
    if(set.has(x-n)) ans++;
    else set.add(n);
}
console.log(ans);