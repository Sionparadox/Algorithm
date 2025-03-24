const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = parseInt(input[0]);
const arr = input[1].split(' ').map(Number);
const score = Array(N).fill(0);
const card = new Map();
for (let i=0; i<N; i++){
    card.set(arr[i],i);
}

for (let i=0;i<N;i++){
    const now = arr[i];
    for(let j=now * 2;j<1000001;j+=now ){
        if(card.has(j)){
            score[card.get(j)]--;
            score[card.get(now)]++;    
        }
    }
}
console.log(score.join(' '));