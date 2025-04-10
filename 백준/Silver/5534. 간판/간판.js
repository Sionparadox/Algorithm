const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = +input[0];
const name = input[1];
const arr = input.slice(2);

let ans = 0;
for (const text of arr){
    if(canMake(text)) ans++;
}
console.log(ans);

function canMake(str){
    for (let i=0; i<str.length; i++){
        if(str[i] != name[0]) continue;
        for (let j=i+1; j<str.length; j++){
            if(str[j] != name[1]) continue;
            const dist = j-i;
            let flag = true;
            for (let k=2; k<name.length; k++) {
                if (str[i + k*dist] != name[k]) {
                    flag = false;
                    break;
                }
            }
            if(flag) return true;
        }
    }
    return false;
}