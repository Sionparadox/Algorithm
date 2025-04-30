const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [[N, T], ...arr] = input.map(v => v.split(' ').map(Number));

let s = Infinity;
let e = 0;

for(const [l, r] of arr){
    if(s > l) s = l;
    if(e < r) e = r;
}
let ans = -1;
while (s <= e){
    const mid = Math.floor((s+e)/2);
    if(isPossible(mid)){
        ans = mid;
        e=mid-1;
    } else{
        s=mid+1;
    }
    
}

console.log(ans);
function isPossible(n) {
    let sum = 0;
    let rest = 0;
    for (const [l, r] of arr) {
        if (n < l) return false;
        sum += l;
        rest += Math.min(r, n) - l;
    }
    return T <= rest + sum && T >= sum;
}