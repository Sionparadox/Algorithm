const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = +input[0];
const desk = input.slice(1).map(v => v.split(' ').map(Number));

const count = Array(6).fill(0);

let prev = new Map();

for (let grade = 1; grade<=5; grade++){
    let cnt = 0;
    for (const [p, q] of desk){
        if (p == grade || q == grade){
            cnt++;
            count[grade] = Math.max(count[grade], cnt);
        } else{
            cnt = 0;
        }
    }
}

let maxCnt = 0;
let minGrade = 6;
for (let i=1; i<=5; i++){
    if(count[i] > maxCnt){
        maxCnt = count[i]
        minGrade = i;
    }
}
console.log(maxCnt, minGrade);