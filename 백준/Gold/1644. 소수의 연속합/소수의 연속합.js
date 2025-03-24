const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = parseInt(input[0]);
const nums = Array(N+1).fill(true);
const prime = [];
for(let i=2;i<=N;i++){
    if(nums[i]){
        prime.push(i)
        for(let j=i*2;j<=N;j += i){
            nums[j] = false;
        }
    }
}

let s=0;
let e=0;
let sum = 0;
let ans = 0;
while(s<=e && e<=prime.length){
    if(sum < N){
        sum += prime[e++];
    } else if(sum > N){
        sum -= prime[s++];
    } else{
        ans++;
        sum = 0;
        s++;
        e=s;
    }
}
console.log(ans);