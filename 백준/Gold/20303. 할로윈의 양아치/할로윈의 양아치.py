import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
candies = list(map(int, input().split()))
parent = [i for i in range(N+1)]

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    rootU = find(u)
    rootV = find(v)
    if rootU != rootV:
        parent[rootV] = rootU

for _ in range(M):
    a, b = map(int, input().split())
    union(a,b)
for node in range(1, N+1):
    find(node)
parent = parent[1:]
groups = {}
for i in range(N):
    root = parent[i]
    if root in groups:
        groups[root][0] += 1
        groups[root][1] += candies[i]
    else:
        groups[root] = [1,candies[i]]

dp = [0]*K

for key in groups:
    cost, value = groups[key]
    for j in range(K-1, cost-1, -1):
        dp[j] = max(dp[j], dp[j-cost]+value)
print(max(dp))
'''
유니언 파인드를 사용해서 친구 그룹 x명 당 사탕 y개를 각각 구함.
이후 해당 그룹들에 대해 냅색 알고리즘으로 최적해를 구함.

dp[i] : i명에게서 뺏을 수 있는 최대 사탕 수
'''