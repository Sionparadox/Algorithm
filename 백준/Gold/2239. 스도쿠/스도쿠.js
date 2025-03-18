const fs = require('fs');
const board = fs.readFileSync(0, 'utf-8').toString().trim().split('\n').map(line => line.split('').map(Number));

backTrack();
console.log(board.map(item => item.join('')).join('\n'));

function backTrack(){
    for (let i=0;i<9;i++){
        for (let j=0;j<9;j++){
            if(board[i][j] == 0){
                for (let n=1;n<=9;n++){
                    if(isAllow(n,i,j)){  
                        board[i][j] = n;
                        if(backTrack()) return true;
                        board[i][j] = 0;
                    }
                }
                return false;
            }
        }
    }
    return true;
}

function isAllow(n,i,j){
    for (let x=0;x<9;x++){
        if(board[x][j] == n) return false;
    }
    for (let y=0;y<9;y++){
        if(board[i][y] == n) return false;
    }
    const baseI = Math.floor(i/3)*3;
    const baseJ = Math.floor(j/3)*3;
    for (let x=baseI;x<3+baseI;x++){
        for (let y=baseJ;y<3+baseJ;y++){
            if(board[x][y] == n) return false;
        }
    }
    return true;
    
}
