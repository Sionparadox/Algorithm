const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');

dr = [-1, 1, 0, 0];
dc = [0, 0, -1, 1];
let idx = 0;
let ans = [];

while (true){
    const N = +input[idx++];
    if(N == 0) break;
    const field = input.slice(idx,idx+N).map(f => f.split(' ').map(Number));
    idx += N;
    ans.push(BFS(N, field));
}
console.log(ans.map((v,i) => `Problem ${i+1}: ${v}`).join('\n'));;

function BFS(N, arr){
    const dist = Array.from({length:N}, () => Array(N).fill(Infinity));
    dist[0][0] = arr[0][0];
    const queue = [[dist[0][0], 0, 0]];
    
    while(queue.length>0){
        queue.sort((a,b) => a[0]-b[0]);
        const [v, r, c] = queue.shift();
        if(r == N-1 && c == N-1){
            return v;
        }
        for (let d=0; d<4; d++){
            const nr = r+dr[d];
            const nc = c+dc[d];
            if(nr>=N || nr<0 || nc>=N || nc<0) continue;
            const nv = v + arr[nr][nc];
            if(nv < dist[nr][nc]){
                dist[nr][nc] = nv;
                queue.push([nv, nr, nc]);
            }
        }
    }
    return dist[N-1][N-1];
}