const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();
const [a, b] = input.split(' ').map(Number);

for (let i=a; i<b+1; i++){
    if(isPalindrom(i+'') && isPrime(i)) console.log(i);
}
console.log(-1);

function isPrime(n){
    for (let i=2; i<Math.sqrt(n)+1; i++){
        if(n % i == 0) return false;
    }
    return true;
}

function isPalindrom(s){
    for (let i=0; i<Math.floor(s.length/2); i++){
        if(s[i] != s[s.length-i-1]) return false;
    }
    return true;
}