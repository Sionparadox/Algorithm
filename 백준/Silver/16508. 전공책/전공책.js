const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
const word = input[0];
const N = +input[1];
const book = input.slice(2).map((b) => {
  const [price, title] = b.split(' ');
  return [+price, title];
});

const neededChars = {};
for (const char of word) {
  neededChars[char] = (neededChars[char] || 0) + 1;
}

let minCost = Infinity;

function backtrack(index, selectedBooks, currentCost) {
  if (currentCost >= minCost) {
    return;
  }

  if (index === N) {
    const combinedChars = {};
    for (const bookIndex of selectedBooks) {
      const title = book[bookIndex][1];
      for (const char of title) {
        combinedChars[char] = (combinedChars[char] || 0) + 1;
      }
    }

    let canMake = true;
    for (const char in neededChars) {
      if (!combinedChars[char] || combinedChars[char] < neededChars[char]) {
        canMake = false;
        break;
      }
    }

    if (canMake) {
      minCost = Math.min(minCost, currentCost);
    }
    return;
  }

  selectedBooks.push(index);
  backtrack(index + 1, selectedBooks, currentCost + book[index][0]);
  selectedBooks.pop();

  backtrack(index + 1, selectedBooks, currentCost);
}

backtrack(0, [], 0);

console.log(minCost === Infinity ? -1 : minCost);
