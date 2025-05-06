const fs = require('fs');
const [str, explode] = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');

const len = explode.length;
const stack = [];
for (const c of str){
    stack.push(c);
    if(stack.length < len || stack.slice(-len).join('') != explode) continue;
    for(let i=0; i<len; i++) stack.pop();
}
console.log(stack.length == 0 ? 'FRULA' : stack.join(''));