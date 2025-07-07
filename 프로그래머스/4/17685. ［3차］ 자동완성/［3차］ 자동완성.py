class Node:
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        curr_node = self.head
        for c in string:
            if c not in curr_node.children:
                curr_node.children[c] = Node(c)
            curr_node = curr_node.children[c]
            curr_node.count += 1
        
        curr_node.data = string
    
    def search(self, query):
        curr_node = self.head
        cnt = 0
        for c in query:
            cnt += 1
            curr_node = curr_node.children[c]
            if curr_node.count == 1:
                return cnt
                    
        return len(query)
        
def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)
    for word in words:
        answer += trie.search(word)
    return answer