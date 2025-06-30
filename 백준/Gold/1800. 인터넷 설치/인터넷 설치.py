import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, P, K = map(int, input().split())

graph = defaultdict(list)
for _ in range(P):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


def check(limit):
    dp = [float('inf')]*(N+1)
    dp[1] = 0
    queue = deque([(1, 0)])
    while queue:
      node, cnt = queue.popleft()
      for nxt, cost in graph[node]:
        temp = 0
        if cost > limit:
            temp += 1
        if dp[nxt] > cnt+temp:
            dp[nxt] = cnt+temp
            queue.append((nxt, cnt+temp))
    
    return dp[N] <= K

s = 0
e = 1000000
answer = -1
while s<=e:
    mid = (s+e)//2
    if check(mid):
        e = mid-1
        answer = mid
    else:
        s = mid+1
print(answer)

'''
가격에 대해 이분탐색.
mid를 구해서 mid 이상의 간선을 K개 이하로 사용하는지 계산
(mid 이하는 어차피 공짜, mid보다 큰 K개는 공짜로 만들 수 있음.)
'''
