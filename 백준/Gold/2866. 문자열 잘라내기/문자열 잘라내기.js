const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const [R, C] = input[0].split(' ').map(Number);
const words = input.slice(1);

const columns = Array.from({ length: C }, (_, c) => 
    words.map(row => row[c]).join('')
);

let cnt = 0;
while (cnt < R) {
    const set = new Set();
    for (let c = 0; c < C; c++) {
        const substr = columns[c].slice(cnt);
        if (set.has(substr)) {
            console.log(cnt - 1);
            return;
        }
        set.add(substr);
    }
    cnt++;
}
console.log(cnt - 1);