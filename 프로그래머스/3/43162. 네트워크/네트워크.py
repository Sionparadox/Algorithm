
def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    ru, rv = find(u), find(v)
    if ru != rv:
        parent[rv] = ru

def solution(n, computers):
    global parent
    parent = [i for i in range(n)]
    
    for i in range(n-1):
        for j in range(i+1,n):
            if computers[i][j] == 1:
                union(i, j)
    
    answer = len(set(map(find, parent)))
    
    
    return answer

