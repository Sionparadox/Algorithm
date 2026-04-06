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
        for nxt in arr:
            curr = curr.children[nxt]
        curr.is_finish = True
        
    
    def check(self, line):
        curr = self.root
        res = []
        for i in range(len(line)):
            nxt = line[i]
            if curr.is_finish:
                res.append(i)
            if nxt in curr.children:            
                curr = curr.children[nxt]
            else:
                break
            
        if curr.is_finish:
            res.append(len(line))
        return res
            

C, N = map(int, input().split())
colors = Trie()
names = set()
for _ in range(C):
    colors.insert(input().strip())
for _ in range(N):
    names.add(input().strip())

Q = int(input())
for _ in range(Q):
    team = input().strip()
    indexes = colors.check(team)
    if not indexes:
        print("No")
        continue
    answer = "No"
    for idx in indexes:
        if team[idx:] in names:
            answer = "Yes"
            break
    print(answer)

'''
색명이 겹칠 수 있음 ex) red, redorange
가능한 경우를 전부 배열로 리턴
'''