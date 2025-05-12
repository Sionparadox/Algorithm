const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const L = +input[0];

const M = 1234567891
let ans = 0;
let R = 1;
for (let i=0; i<L; i++){
    ans = (ans + (input[1].charCodeAt(i)-96) * R) % M;
    R = (R * 31) % M;
}
console.log(ans);