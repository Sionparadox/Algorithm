const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();
let ans = [];
if(input.includes('::')){
    const [l, r] = input.split('::');
    const left = l.split(':');
    const right = r.split(':');
    ans = [...left, ...Array(8 - left.length - right.length).fill('0'), ...right];
} else {
    ans = input.split(':');
}
console.log(ans.map(ip => ip.padStart(4, '0')).join(':'));