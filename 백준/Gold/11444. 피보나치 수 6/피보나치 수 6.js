const fs = require('fs');
let N = BigInt(fs.readFileSync(0, 'utf-8').toString().trim());

const BIGNUM = 1000000007n;

let ans = [[1n,0n],[0n,1n]];
let mat = [[1n,1n],[1n,0n]];
while (N > 0n){
    if(N % 2n === 1n){
        ans = multiply(ans, mat);
    }
    mat = multiply(mat, mat);
    N = N / 2n;
}

console.log(ans[0][1].toString());

function multiply(a, b){
    return [
        [
            (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % BIGNUM,
            (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % BIGNUM
        ],
        [
            (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % BIGNUM,
            (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % BIGNUM
        ]
    ];
}
