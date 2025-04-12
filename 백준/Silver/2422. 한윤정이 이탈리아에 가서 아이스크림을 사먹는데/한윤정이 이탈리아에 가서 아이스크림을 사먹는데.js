const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [[N, M], ...arr] = input.map(v => v.split(' ').map(Number));

const disjoint = Array.from({length : N+1}, () => Array(N+1).fill(false));
for (const [u, v] of arr){
    disjoint[u][v] = true;
    disjoint[v][u] = true;
}

let ans = 0;
for (let i=1; i<N-1; i++){
    for (let j=i+1; j<N; j++){
        if(disjoint[i][j]) continue;
        for (let k=j+1; k<N+1; k++){
            if(!disjoint[i][k] && !disjoint[j][k]) ans++;
        }
    }
}
console.log(ans);