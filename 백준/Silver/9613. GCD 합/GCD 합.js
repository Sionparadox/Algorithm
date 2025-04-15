const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const T = +input[0];
const nums = input.slice(1).map(v => v.split(' ').map(Number));

const ans = [];
for (let t=0; t<T; t++){
    const number = nums[t].slice(1);
    const N = nums[t][0];
    let res= 0;
    for (let i=0; i<N-1; i++){
        for (let j=i+1; j<N; j++){
            res+= GCD(number[i], number[j]);
        }
    }
    ans.push(res);
}
console.log(ans.join('\n'));

function GCD(x, y){
    if(y == 0) return x;
    return GCD(y, x%y);
}