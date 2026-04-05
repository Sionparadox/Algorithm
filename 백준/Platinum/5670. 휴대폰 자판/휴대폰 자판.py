import sys
from collections import defaultdict
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_finish = False

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, arr):
        curr = self.root
        for child in arr:
            curr = curr.children[child]

        curr.is_finish = True
    
    def count(self, word):
        curr = self.root
        cnt = 0
        for child in word:
            if curr == self.root or len(curr.children) > 1 or curr.is_finish:
                cnt += 1
            curr = curr.children[child]
        
        return cnt

while True:
    _input = input().strip()
    if not _input:
        break
    
    N = int(_input)
    trie = Trie()
    words = []
    for _ in range(N):
        word = input().strip()
        trie.insert(word)
        words.append(word)
        
    tot = 0
    for word in words:
        tot += trie.count(word)
    
    print(f'{tot/N:.2f}')



'''
트라이로 만들어서 저장
눌러야 하는 경우
- 첫 글자일 경우
- 다음 글자가 여러개일 경우
- 현재 위치에서 끝나는 글자가 있을 경우
'''
