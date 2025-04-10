const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [[M, N], ...board] = input.map(v => v.split(' ').map(Number));

const visited = Array.from({length:M}, () => Array(N).fill(false));

let ans = 0;
const dr = [-1, -1, -1, 0, 0, 1, 1, 1];
const dc = [-1, 0, 1, -1, 1, -1, 0, 1];
for (let i=0; i<M; i++){
    for(let j=0; j<N; j++){
        if(!visited[i][j] && board[i][j] == 1){
            dfs(i, j);
            ans++;
        }
    }
}
console.log(ans);

function dfs(r, c){
    visited[r][c] = true;
    for (let d=0;d<8;d++){
        const newR = r+dr[d];
        const newC = c+dc[d];
        if (newR < 0 || newR >= M || newC < 0 || newC >= N) continue;
        if(!visited[newR][newC] && board[newR][newC] == 1){
            dfs(newR, newC);
        }
    }
}