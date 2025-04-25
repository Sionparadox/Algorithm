const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();
const [N, M] = input.split(' ').map(Number);


ans = '';
backTrack(0, []);
function backTrack(k, str){
    if (k == M){
        ans += str+'\n';
        return;
    }
    
    for (let i=1; i<=N; i++){
        backTrack(k+1, ''+str+i+' ');
    }
}

console.log(ans);
