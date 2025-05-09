const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim();
const stack = [];
const ans = [];
for (const c of input){
    if(c == '+' || c == '-'){
        while(stack.length > 0){
            const ops = stack.pop();
            if(ops == '('){
                stack.push(ops);
                break;
            }
            ans.push(ops);
        }
        stack.push(c);
    }
    else if(c == '*' || c == '/'){
        if(stack.at(-1) == '*' || stack.at(-1) == '/'){
            const ops = stack.pop();
            ans.push(ops);
        }
        stack.push(c);
    }
    else if(c == '(') stack.push(c);
    else if(c == ')'){
        while(true){
            const ops = stack.pop();
            if(ops == '(') break;
            ans.push(ops);
        }
    }
    else ans.push(c);
}

while(stack.length>0){
    ans.push(stack.pop());
}
console.log(ans.join(''));