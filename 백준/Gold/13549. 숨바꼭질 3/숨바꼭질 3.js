const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();
const [N, K] = input.split(' ').map(Number);
const MAX = Math.max(N, K) * 2 + 1
const visited = Array(MAX).fill(Infinity);
visited[N] = 0;
const queue = [N];
let head = 0;

while (head < queue.length){
    const pos = queue[head++];
    const time = visited[pos];
    if(pos == K){
        console.log(time);
        break;
    }
    
    if (pos * 2 <= MAX && visited[pos * 2] === Infinity) {
        visited[pos * 2] = time;
        queue.push(pos * 2);
    }
    
    if (pos - 1 >= 0 && visited[pos - 1] === Infinity) {
        visited[pos - 1] = time + 1;
        queue.push(pos - 1);
    }

    if (pos + 1 <= MAX && visited[pos + 1] === Infinity) {
        visited[pos + 1] = time + 1;
        queue.push(pos + 1);
    }
    
}