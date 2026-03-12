import sys
input = sys.stdin.readline

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    rng = [tuple(map(int, input().split())) for _ in range(M)]
    rng.sort(key=lambda x:x[1])
    
    parent = list(range(N+2))
    answer = 0
    
    for left, right in rng:
        book = find(left)
        if book <= right:
            answer += 1
            parent[book] = find(book+1)
    
    print(answer)


'''
N<=1000 이므로 N^2으로도 풀림
union-find사용해 경로압축 가능
'''