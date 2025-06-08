import sys
from collections import defaultdict
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.isFinish = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, arr):
        curr = self.root
        for child in arr:
            if curr.isFinish:
                return False
            curr = curr.children[child]
            
        if curr.children:
            return False
        curr.isFinish = True
        return True

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [input().strip() for _ in range(N)]
    trie = Trie()
    answer = "YES"
    for tel in arr:
        if not trie.insert(tel):
            answer = "NO"
            break
    print(answer)