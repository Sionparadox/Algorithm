import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = defaultdict(list)
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(N+1)]

def DFS(node, parent):
    dp[node][0] = 0
    dp[node][1] = 1
    for next in graph[node]:
        if next == parent:
            continue
        DFS(next, node)
        dp[node][0] += dp[next][1]
        dp[node][1] += min(dp[next][0], dp[next][1])

DFS(1, 0)
print(min(dp[1]))
'''
dp[i][0] : i번 노드가 얼리어답터가 아닐 때 얼리어답터의 수
dp[i][1] : i번 노드가 얼리어답터일 때 얼리어답터의 수

본인이 얼리어답터일 경우 자식은 얼리어답터가 아니어도 됨
본인이 얼리어답터가 아니라면 자식은 얼리어답터여야함
'''