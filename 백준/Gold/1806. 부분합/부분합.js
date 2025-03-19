const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [N, S] = input[0].split(' ').map(Number);
const seq = input[1].split(' ').map(Number);

let p1 = 0;
let p2 = 0;
let minLen = 100000;
let partSum = seq[p1];
while (p2 < N){
    if(partSum >= S){
        minLen = Math.min(minLen, p2 - p1 + 1);
        partSum -= seq[p1++];
    } else {
        partSum += seq[++p2] ?? 0;
    }
}
minLen = minLen == 100000 ? 0 : minLen;
console.log(minLen);