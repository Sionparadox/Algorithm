import sys
from collections import defaultdict
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, arr):
        curr = self.root
        for child in arr:
            curr = curr.children[child]
    
    def show(self, node=None, depth=0):
        if node == None:
            node = self.root
        for k in sorted(node.children):
            print('--'*depth+k)
            self.show(node.children[k], depth+1)

N = int(input())
trie = Trie()
for _ in range(N):
    foods = input().split()[1:]
    trie.insert(foods)

trie.show()

'''
트라이 자료구조 사용
Node 클래스의 자식 : 딕셔너리(자식 문자열, Node)
'''