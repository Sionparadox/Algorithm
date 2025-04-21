const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();
const [N, L, W, H] = input.split(' ').map(Number);

let s = 0.0;
let e = Math.max(L, W, H);

for (let t=0; t<100;t++){
    let mid = (s+e) / 2;
    if(Math.floor(L/mid) * Math.floor(W/mid) * Math.floor(H/mid) >= N){
        s = mid;
    } else {
        e = mid;
    }
}
console.log(s.toFixed(10));