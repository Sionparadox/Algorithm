const fs = require('fs');
const [N, K] = fs.readFileSync(0, 'utf-8').toString().trim().split(' ').map(Number);

const visited = Array(100001).fill(-1);
const cnt = Array(100001).fill(0);
const queue = [N];
visited[N] = 0;
cnt[N] = 1;

while(queue.length > 0){
    const pos = queue.shift();
    
    for(const next of [pos-1, pos+1, pos*2]){
        if(next < 0 || next > 100000) continue;
        if(visited[next] == -1){
            visited[next] = visited[pos]+1;
            cnt[next] = cnt[pos];
            queue.push(next);
        }
        else if(visited[next] == visited[pos]+1){
            cnt[next] += cnt[pos];
        }
        
    }
}
console.log(visited[K]);
console.log(cnt[K])