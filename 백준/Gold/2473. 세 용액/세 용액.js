const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = +input[0];
const acid = input[1].split(' ').map(Number);
acid.sort((a,b) => a-b);

let minDiff = Infinity;
let ans = '';
for (let i=0; i<N-2; i++){
    let s = i+1;
    let e = N-1;
    
    while(s<e){
        const sum = acid[i] + acid[s] + acid[e];
        if(Math.abs(sum) < minDiff){
            minDiff = Math.abs(sum);
            ans = `${acid[i]} ${acid[s]} ${acid[e]}`;
        }
        if(sum < 0) s++
        else e--;
    }
}

console.log(ans);