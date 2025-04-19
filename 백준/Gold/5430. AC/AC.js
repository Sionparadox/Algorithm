const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const T = +input[0];
for (let t=0; t<T; t++){
    const order = input[t*3+1];
    const N = +input[t*3+2];
    let arr = [];
    if(N != 0) arr = input[t*3+3].slice(1,input[t*3+3].length-1).split(',').map(Number);
    let r = true; //앞 -> 뒤
    let flag = false;
    for (const s of order){
        if (s == 'R') r = !r;
        if (s == 'D'){
            if(arr.length == 0){
                flag = true;
                break;
            }
            if(r) arr.shift();
            else arr.pop();
        }
    }
    if(!r) arr.reverse();
    console.log(flag ? 'error' : `[${arr.join(',')}]`);
}
