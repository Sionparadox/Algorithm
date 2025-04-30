const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = parseInt(input[0]);
const pos = input.slice(1).map(item => item.split(' ').map(Number));
pos.push(pos[0]);

let ans = 0;
for (let i=0;i<N;i++){
    ans += pos[i][0] * pos[i+1][1];
    ans -= pos[i+1][0] * pos[i][1];
}
console.log(Math.abs(ans/2).toFixed(1));
