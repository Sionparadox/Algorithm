const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = +input[0];
const picture = input.slice(1);

console.log(toStr(press(0, 0, N)));

function press(r, c, size){
    const num = picture[r][c];
    let flag = false;
    for (let i=r; i<r+size; i++){
        for (let j=c; j<c+size; j++){
            if(num != picture[i][j]){
                flag = true;
                break;
            }
        }
        if(flag) break;
    }
    
    if(!flag){
        return num;
    }else{
        const half = Math.floor(size/2);
        return [
            press(r, c, half),
            press(r, c+half, half),
            press(r+half, c, half),
            press(r+half, c+half, half)
        ];
    }
}


function toStr(arr){
    if(typeof arr == 'string') return arr;
    return '('+arr.map(toStr).join('')+')';
}