const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [N,M] = input[0].split(' ').map(Number);
const board = input.slice(1, 1+N).map(b => b.split(' ').map(Number));
const pos = input.slice(1+N).map(p => p.split(' ').map(Number));

const prefix = Array.from({length:N+1},() => Array(N+1).fill(0));

for (let i=1; i<=N; i++){
    for (let j=1; j<=N; j++){
        prefix[i][j] = board[i-1][j-1];
        prefix[i][j] += prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1];
    }
}
ans = [];
for (const [x1, y1, x2, y2] of pos){
    ans.push(prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]);
}
console.log(ans.join('\n'));
