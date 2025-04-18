const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();

let ans = '';
for (const s of input){
    if(s === s.toLowerCase()){
        ans += s.toUpperCase();
    } else{
        ans += s.toLowerCase();
    }
}
console.log(ans);