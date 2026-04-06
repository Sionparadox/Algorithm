import sys
from collections import defaultdict
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_finish = False
        self.safe_cnt = 0
        self.delete_cnt = 0

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, line, flag=False):
        curr = self.root
        if flag:
            curr.safe_cnt += 1
        else:
            curr.delete_cnt += 1
            
        for nxt in line:
            curr = curr.children[nxt]
            if flag:
                curr.safe_cnt += 1
            else:
                curr.delete_cnt += 1
        if not flag:
            curr.is_finish = True

    def solve(self, node=None):
        res = 0
        if node == None:
            node = self.root
        if node.safe_cnt == 0:
            return 1
        if node.delete_cnt == 0:
            return 0
        
        if node.is_finish:
            res += 1
        for nxt in node.children.values():
            res += self.solve(nxt)
        
        return res

T = int(input())
for _ in range(T):
    N = int(input())
    trie = Trie()
    for _ in range(N):
        trie.insert(input().strip())
    
    K = int(input())
    for _ in range(K):
        trie.insert(input().strip(), True)
    
    print(trie.solve())

'''
트라이를 사용하고
각 노드에 지워야할 개수, 지우지 말아야할 개수를 기록하며 삽입하기
이후 트라이 전체를 dfs로 탐색하며 개수 세기
'''