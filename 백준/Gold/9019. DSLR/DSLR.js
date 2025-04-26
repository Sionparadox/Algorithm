const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const T = +input[0];

for (let t=1; t<=T; t++){
    const [A, B] = input[t].split(' ').map(Number);
    const visited = Array(10000).fill(false);
    const queue = [];
    
    queue.push([A, '']);
    visited[A] = true;
    
    while(queue.length >0){
        const [num, ord] = queue.shift();
        if(num == B){
            console.log(ord);
            break;
        }
        for (const o of ['D', 'S', 'L', 'R']){
            const next = calc(num, o);
            if(!visited[next]){
                visited[next] = true;
                queue.push([next, ord+o]);
            }
        }
    }
    
    
}


function calc(num, order){
    if(order == 'D') return (num * 2) % 10000;
    if(order == 'S') return num == 0 ? 9999 : num-1;
    if(order == 'L') return Math.floor(num/1000) + (num % 1000) * 10;
    return Math.floor(num/10) + (num%10) * 1000;
    
}