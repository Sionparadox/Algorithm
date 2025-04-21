const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = +input[0];
const card = input[1].split(' ').map(Number);
const MAX_K = Math.floor(Math.log2(N));

const number = Array.from({length : N}, (_,i) => i+1);
for (let i=1; i<=MAX_K; i++){
    for(let j=1; j<=MAX_K; j++){
        let deck = [...number];
        deck = suffle(i,N, deck);
        deck = suffle(j,N, deck);
        if(deck.join('') == card.join('')){
            console.log(i,j);
            return;
        }
    }
}

function suffle(k, end, arr){
    let deck = [...arr];
    for (let i=1; i<=k+1; i++){
        const cnt = Math.pow(2, k-i+1);
        const temp = deck.splice(end-cnt,cnt);
        deck = [...temp, ...deck];
        end = cnt;
    }
    return deck;
}