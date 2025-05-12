const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const L = +input[0];

let ans = 0;
for (let i=0; i<L; i++){
    ans += (input[1].charCodeAt(i)-96)*Math.pow(31, i) % 1234567891;
    ans %= 1234567891
}
console.log(ans);