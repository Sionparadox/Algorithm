import sys
input = sys.stdin.readline

N = int(input())
parent = list(range(N+1))
size = [1]*(N+1)

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def get_pair(node):
    p = find(node)
    return size[p] * (size[p]-1)//2
    
        
def get_bridge(node):
    p = find(node)
    s = size[p]
    return (s**3 - s)//6


pair = bridge = 0
for _ in range(N-1):
    k = int(input())
    u, v = find(k), find(k+1)
    
    if u != v:
        pair -= get_pair(u)
        pair -= get_pair(v)
        
        bridge -= get_bridge(u)
        bridge -= get_bridge(v)
        
        parent[v] = u
        size[u] += size[v]
        
        pair += get_pair(u)
        bridge += get_bridge(u)
    print(pair, bridge)
    

'''
(i, j) 쌍 : 그룹 크기 s, sC2
다리개수 합 : 그룹 크기 : s, (s-1)*1+(s-2)*2+(s-3)*3 ... (s-1만큼 반복)
-> s * (1~s-1까지 합) - (1~s-1까지 제곱의 합)
n*n*(n-1)//2 - (n-1)*(n)(2n-1)//6
= (3n^3 - 3n^2 - 2n^3 +3n^2 - n) // 6
= (n^3-n)//6
'''