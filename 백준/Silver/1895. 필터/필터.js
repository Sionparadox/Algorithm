const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [R, C] = input[0].split(' ').map(Number);
const image = input.slice(1, 1+R).map(v => v.split(' ').map(Number));
const T = +input[1+R];

let ans = 0;
for (let i=0; i<R-2; i++){
    for (let j=0; j<C-2; j++){
        const temp = [...image[i].slice(j,j+3), 
        ...image[i+1].slice(j,j+3), 
        ...image[i+2].slice(j,j+3)]
        temp.sort((a,b) => a-b);
        if(temp[4] >= T) ans++;
    }
}

console.log(ans);