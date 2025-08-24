import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
populations = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(N-1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*N
dp = [[0]*2 for _ in range(N)]

def DFS(node):
    visited[node] = True
    dp[node][1] = populations[node]
    for child in graph[node]:
        if visited[child]: continue
        DFS(child)
        dp[node][1] += dp[child][0]
        dp[node][0] += max(dp[child])

DFS(0)
print(max(dp[0]))

'''
10001처럼 연속된 비우수가 3개이상 발생하면 안되는데
최대를 구하면 어차피 10101이 반드시 10001보다 더 크므로
문제 조건이 무의미해짐 -> 최대값을 가지는 트리의 독립집합 문제와 동일 문제
'''