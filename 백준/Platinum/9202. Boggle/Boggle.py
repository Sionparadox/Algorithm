import sys
from collections import defaultdict
input = sys.stdin.readline

directions = [(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]
score = {1:0, 2:0, 3:1, 4:1, 5:2, 6:3, 7:5, 8:11}

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_finish = False
        self.word = ''



class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, line):
        curr = self.root
        for nxt in line:
            curr = curr.children[nxt]
        curr.is_finish = True
        curr.word = line
    
def backtrack(r, c, node, depth):
    if node.is_finish:
        words.add(node.word)
    if depth == 8:
        return
    
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<0 or nr>3 or nc<0 or nc>3:
            continue
        if visited[nr][nc]:
            continue
        
        nxt = board[nr][nc]
        if nxt in node.children:
            visited[nr][nc] = True
            backtrack(nr, nc, node.children[nxt], depth+1)
            visited[nr][nc] = False
        


W = int(input())
trie = Trie()
for _ in range(W):
    trie.insert(input().strip())

input()
B = int(input())

for b in range(B):
    board = [input().strip() for _ in range(4)]
    input()

    visited = [[False]*4 for _ in range(4)]
    words = set()
    for r in range(4):
        for c in range(4):
            ch = board[r][c]
            if ch in trie.root.children:
                visited[r][c] = True
                backtrack(r, c, trie.root.children[ch], 1)
                visited[r][c] = False
    word_list = sorted(list(words), key = lambda x:(-len(x), x))
    sc = sum(score[len(x)] for x in word_list)
    print(sc, word_list[0], len(word_list))
    

'''
단어 정보를 트라이에 저장한 후
16칸의 보드로 백트래킹 진행
'''

