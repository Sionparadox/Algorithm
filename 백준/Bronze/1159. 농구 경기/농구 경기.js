const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = +input[0];

const alpha = Array(26).fill(0);
for (const s of input.slice(1)){
    alpha[s.charCodeAt(0)-97]++;
}
let ans =''
for (let i=0; i<26; i++){
    if(alpha[i] >= 5) ans += String.fromCharCode(i+97);
}
console.log(ans == '' ? 'PREDAJA' : ans);