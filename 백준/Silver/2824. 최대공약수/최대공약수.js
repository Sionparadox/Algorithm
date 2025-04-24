const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = +input[0];
const A = input[1].split(' ').map(Number);
const M = +input[2];
const B = input[3].split(' ').map(Number);

const limit = Math.max(...A, ... B);
const sqrtLimit = Math.floor(Math.sqrt(limit));
const isPrime = Array(sqrtLimit+1).fill(true);
isPrime[0] = isPrime[1] = false;

for (let i=2; i<= sqrtLimit; i++){
    if(isPrime[i]){
        for (let j=i*i; j<=sqrtLimit; j+= i){
            isPrime[j] = false;
        }
    }
}

const factorA = getFactor(A);
const factorB = getFactor(B);

let res = 1n;
for (const [p, cnt] of factorA.entries()){
    if(factorB.has(p)){
        const minVal = Math.min(cnt, factorB.get(p));
        res *= BigInt(p) ** BigInt(minVal);
    }
}
console.log(res > 999999999 ? res.toString().slice(-9) : res.toString());


function getFactor(arr){
    const map = new Map();
    for (let n of arr){
        for (let i=2; i<=Math.sqrt(limit); i++){
            if(isPrime[i]){
                let cnt = 0;
                while(n%i == 0){
                    n /= i;
                    cnt++;
                }
                if(cnt > 0) map.set(i, (map.get(i) || 0) + cnt);
            }
        }
        if(n>1) map.set(n, (map.get(n) || 0) + 1);
    }
    return map;
}