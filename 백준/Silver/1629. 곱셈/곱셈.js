const fs = require('fs');
const [A,B,C] = fs.readFileSync(0, 'utf-8').toString().trim().split(' ').map(BigInt);
console.log(power(A,B,C).toString());

function power(num,exp,mod){
    if(exp == 0n) return 1n;
    
    if(exp % 2n == 1n) return (num * power(num,exp-1n,mod))%mod;
    
    const half = power(num,exp/2n,mod);
    return (half*half)%mod;
}