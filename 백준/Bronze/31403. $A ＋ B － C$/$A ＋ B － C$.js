const fs = require('fs');
const [A,B,C] = fs.readFileSync(0,'utf-8').toString().trim().split('\n');
console.log(parseInt(A)+parseInt(B)-C);
console.log(A+B-C);