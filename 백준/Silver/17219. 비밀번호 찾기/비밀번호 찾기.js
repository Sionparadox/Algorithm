const fs = require('fs');
const input = fs.readFileSync(0,'utf-8').toString().trim().split('\n');
const [N,M] = input[0].split(' ').map(Number);
const map = new Map();
for (const str of input.slice(1,1+N)){
    const [site, pwd] = str.split(' ');
    map.set(site,pwd);
}
for (const s of input.slice(1+N)){
    console.log(map.get(s));
}
