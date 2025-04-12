const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();
const [X, Y] = input.split(' ').map(Number);

let diff = Y-X;
let inc = 1;
let cnt = 0;
while (diff > 0){
    diff -= inc;
    cnt++;
    if (diff <= 0) break;
    diff -= inc;
    cnt++;
    inc++;
}
console.log(cnt);
