const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const T = +input[0];

let line = 1;
for (let t=0; t<T; t++){
    const [N, d] =  input[line++].split(' ').map(Number);
    let board = input.slice(line, line+N).map(v => v.split(' ').map(Number));
    line += N;
    const K = ((d+360) % 360)/45;
    for (let k=0; k<K; k++){
       board = rotate(board);
    }
    console.log(board.map(v=>v.join(' ')).join('\n'));
}

function rotate(arr){
    const N = arr.length;
    const mid = Math.floor(N/2);
    let res = arr.map(r => [...r]);
    for (let i=0; i<N; i++){
        res[i][mid] = arr[i][i];
        res[i][N-i-1] = arr[i][mid];
        res[mid][i] = arr[N-i-1][i];
        res[i][i] = arr[mid][i];
    }
    return res;
}