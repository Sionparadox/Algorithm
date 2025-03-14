const fs = require('fs');
const input = fs.readFileSync(0,'utf-8').toString().trim().split('\n');
const N = parseInt(input[0]);
const tree = new Map();
for (const str of input.slice(1)){
    const [root,left,right] = str.split(' ');
    tree.set(root,{'root':root,'left':left,'right':right});
}
console.log(preOrder('A'));
console.log(inOrder('A'));
console.log(postOrder('A'));

function preOrder(c){
    if (c == '.') return '';
    const node = tree.get(c);
    return c+preOrder(node.left) + preOrder(node.right)
    
}

function inOrder(c){
    if (c == '.') return '';
    const node = tree.get(c);
    return inOrder(node.left) + c + inOrder(node.right);
}

function postOrder(c){
    if(c == '.') return '';
    const node = tree.get(c);
    return postOrder(node.left) + postOrder(node.right) + c;
}