import sys
from collections import defaultdict, deque
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_finish = False
        self.fail = None

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for nxt in word:
            curr = curr.children[nxt]
        curr.is_finish = True
    
    def build(self):
        self.root.fail = self.root
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            
            for ch in curr.children:
                nxt = curr.children[ch]
                if curr == self.root:
                    nxt.fail = self.root
                
                else:
                    fail_node = curr.fail
                    
                    while fail_node != self.root and ch not in fail_node.children:
                        fail_node = fail_node.fail
                    
                    if ch in fail_node.children:
                        nxt.fail = fail_node.children[ch]
                    else:
                        nxt.fail = self.root
                
                if nxt.fail.is_finish:
                    nxt.is_finish = True
                
                queue.append(nxt)
        
    def find(self, word):
        curr = self.root
        
        for ch in word:
            while curr != self.root and ch not in curr.children:
                curr = curr.fail
            
            if ch in curr.children:
                curr = curr.children[ch]
            
            if curr.is_finish:
                return True
        return False
            

N = int(input())
trie = Trie()
for _ in range(N):
    trie.insert(input().strip())

trie.build()

Q = int(input())
for _ in range(Q):
    print("YES" if trie.find(input().strip()) else "NO")


'''
아호-코라식 : 트라이 + KMP알고리즘
트라이에 fail함수가 추가됨
트라이 완성 후 build를 통해 fail노드에 대한 정보를 추가해줌. (BFS)
이후 탐색할때에도 자식이 없으면 fail을 거슬러 올라가며 현재 노드를 업데이트
'''