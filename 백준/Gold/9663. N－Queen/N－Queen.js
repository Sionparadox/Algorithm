const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();
const N = +input;

const visited = Array.from({length: N}, () => Array(N).fill(false));
const dr = [-1, -1, -1, 0, 1, 1, 1, 0];
const dc = [-1, 0, 1, 1, 1, 0, -1, -1];

let ans = 0;
backTrack(0);
console.log(ans);

function backTrack(r){
    if(r == N){
        ans++;
        return;   
    }   
    for (let i=0; i<N; i++){
        if(!visited[r][i] && noQueen(r, i)){
            visited[r][i] = true;
            backTrack(r+1);
            visited[r][i] = false;
        }
    }
}


function noQueen(r, c){
    for (let i=0; i<8; i++){
        let [nr, nc] = [r, c];
        while (nr >= 0 && nc >= 0 && nr<N && nc <N){
            if(visited[nr][nc]) return false;
            nr += dr[i];
            nc += dc[i];
        }
    }
    
    return true;
}


// [2,4]
// (0,2) , (1,3) , (2,4) , (3,5) , (4,6) , (5,7) , (6,8)
// (0,6) , (1,5) , (2,4) , (3,3) , (4,2) , (5,1) , (6,0)


// [4,2]
// (2,0) , (3,1) , (4,2) , (5,3) , (6,4) , (7,5) , (8,6)
// (6,0) , (5,1) , (4,2) , (3,3) , (2,4) , (1,5) , (0,6)