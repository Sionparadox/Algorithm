const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');

for (let t=0; t<3; t++){
    const [start, end] = input[t].split(' ').map(v => v.split(':').map(Number));
    
    let [h, m, s] = start;
    let cnt = 0;
    while(true){
        if((h + m + s) % 3 == 0) cnt++;
        if(h == end[0] && m == end[1] && s == end[2]) break;
        [h, m, s] = time(h, m, s);
    }
    console.log(cnt);
}

function time(h, m, s){
    s += 1;
    if(s == 60){
        s = 0;
        m += 1;
    }
    if(m == 60){
        m = 0;
        h += 1;
    }
    if(h == 24){
        h = 0;
    }
    return [h, m, s];
}