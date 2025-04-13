const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const nums = input[1].split(' ').map(Number);

nums.sort((a, b) => a - b);
const ans = [];
makeSeq([]);
console.log(ans.join('\n'));

function makeSeq(arr){
    if(arr.length == M) {
        ans.push(arr.join(' '));
        return;
    }
    
    for(let i=0; i<N; i++){
        arr.push(nums[i])
        makeSeq(arr);
        arr.pop();
    }
}