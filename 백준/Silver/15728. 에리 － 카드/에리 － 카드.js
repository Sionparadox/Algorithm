const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [N, K] = input[0].split(' ').map(Number);
const share = input[1].split(' ').map(Number);
const team = input[2].split(' ').map(Number);

const removed = new Set();
for (let k=0; k<K; k++){
    let maxNum = -Infinity;
    let idx = -1;
    for (const t of team){
        if(removed.has(t)) continue;
        for (const s of share){
            if (maxNum < t*s){
                maxNum = t*s;
                idx = t;
            }
        }
    }
    removed.add(idx);
}

let ans = -Infinity;
for (const t of team){
    if(removed.has(t)) continue;
    for (const s of share){
        ans = Math.max(ans, s*t);
    }
}

console.log(ans);

