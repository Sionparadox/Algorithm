const fs = require('fs');
const input = fs.readFileSync(0,'utf-8').toString().trim().split(' ').map(Number);
let flag = input[0] < input[1];
for (let i=0;i<7;i++){
    if(flag != (input[i] < input[i+1])){
        console.log("mixed");
        process.exit(0);
    }
}
if(flag){
    console.log("ascending");
} else{
    console.log("descending");
}