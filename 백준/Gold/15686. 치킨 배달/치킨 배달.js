const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [[N, M], ...city] = input.map(v => v.split(' ').map(Number));
const chicken = [];
for (let i=0; i<N; i++){
    for (let j=0; j<N; j++){
        if(city[i][j] == 2){
            chicken.push([i,j]);
        }
    }
}

let ans = Infinity;
dfs(0,[]);
console.log(ans);

function dfs(idx, arr){
    if(arr.length == M){
        ans = Math.min(ans, calc(arr));
        return; 
    }
    
    for (let i=idx; i<chicken.length; i++){
        arr.push(chicken[i]);
        dfs(i+1, arr);
        arr.pop();
    }
    
}

function calc(arr){
    let res = 0;
    for (let i=0; i<N; i++){
        for (let j=0; j<N; j++){
            if(city[i][j] == 1){
                let temp = Infinity;
                for (const [x, y] of arr){
                    temp = Math.min(temp, Math.abs(i-x) + Math.abs(j-y));
                }
                res += temp;
            }
        }
    }
    return res;
}