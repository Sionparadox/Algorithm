const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const str = input.map(v => v.split(''));

ans = '';
for (let i=0; i<15; i++){
    for (let j=0; j<5; j++){
        if(str[j].length <=i) continue;
        ans += str[j][i];
    }
}
console.log(ans);