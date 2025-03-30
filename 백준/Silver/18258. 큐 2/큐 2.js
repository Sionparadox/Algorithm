const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');
// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
const N = +input[0];

class Queue {
  constructor() {
    this.queue = [];
    this.head = 0;
  }

  push(n) {
    this.queue.push(n);
  }

  pop() {
    return this.empty() ? -1 : this.queue[this.head++];
  }

  size() {
    return this.queue.length - this.head;
  }

  empty() {
    return this.queue.length == this.head;
  }

  front() {
    return this.queue[this.head] ?? -1;
  }

  back() {
    return this.empty() ? -1 : this.queue.at(-1);
  }
}

const q = new Queue();
const ans = [];
for (let i = 1; i <= N; i++) {
  const [order, k] = input[i].split(' ');
  switch (order) {
    case 'push':
      q.push(k);
      break;
    case 'pop':
      ans.push(q.pop());
      break;
    case 'size':
      ans.push(q.size());
      break;
    case 'empty':
      ans.push(q.empty() ? 1 : 0);
      break;
    case 'front':
      ans.push(q.front());
      break;
    case 'back':
      ans.push(q.back());
      break;
    default:
      break;
  }
}

console.log(ans.join('\n'));
