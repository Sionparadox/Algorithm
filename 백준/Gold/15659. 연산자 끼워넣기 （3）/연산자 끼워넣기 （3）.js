const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const N = +input[0];
const nums = input[1].split(' ').map(Number);
const arr = input[2].split(' ').map(Number); // + - x /

const ops = ['+', '-', '*', '/'];
const op = [];
for (let i=0; i<4; i++){
    while(arr[i]>0){
        op.push(ops[i]);
        arr[i]--;
    }
}

let maxVal = -Infinity;
let minVal = Infinity;

backTrack(op, 0);
console.log(maxVal);
console.log(minVal);

function backTrack(operator, idx){
    if(idx == operator.length){
        let temp = calc(operator);
        maxVal = Math.max(maxVal, temp);
        minVal = Math.min(minVal, temp);
        return;
    }
    
    for (let i=idx; i<N-1; i++){
        [operator[idx], operator[i]] = [operator[i], operator[idx]];
        backTrack(operator, idx+1);
        [operator[idx], operator[i]] = [operator[i], operator[idx]];
    }
}


function operation(x, y, p){
    if(p == '+') return x + y;
    if(p == '-') return x - y;
    if(p == '*') return x * y;
    return Math.floor(x / y);
}

function calc(operator){
    const stack = [nums[0]];
    for (let i=0; i<N-1; i++){
        if(operator[i] == '+' || operator[i] == '-'){
            stack.push(operator[i]);
            stack.push(nums[i+1]);
        } else {
            const lastNum = stack.pop();
            stack.push(operation(lastNum, nums[i+1], operator[i]));
        }
    }
    let ans = stack[0];
    for (let i=1;i<stack.length-1;i+=2){
        ans = operation(ans,stack[i+1], stack[i]);

    }
    return ans;
}