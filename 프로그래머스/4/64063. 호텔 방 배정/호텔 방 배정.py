import sys
sys.setrecursionlimit(10**6)
def solution(k, room_number):
    parent = {}
    def find(node):
        if node not in parent:
            return node
        parent[node] = find(parent[node])
        return parent[node]

    result = []
    for num in room_number:
        room = find(num)
        result.append(room)
        parent[room] = find(room+1)
    
    return result