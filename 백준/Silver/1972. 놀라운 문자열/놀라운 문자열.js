const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');

let line = 0;
while(true){
    const str = input[line++];
    if(str == '*') break;
    let flag = false;
    for (let i=0;i<=str.length-2;i++){
        if(!unique(str,i)){
            flag = true;
            break;
        }
    }
    console.log(str + ' is '+ (flag ? 'NOT ' : '') + 'surprising.')
}


function unique(str, d){
    const set = new Set();
    for (let i=0;i< str.length-d-1; i++){
        set.add(str[i]+str[i+d+1]);
    }
    if(set.size == str.length-d-1) return true;
    return false;
}