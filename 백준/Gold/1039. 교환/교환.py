import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(str(N))
M = len(nums)

visited = [set() for _ in range(K+1)]
n = str(N)
queue = deque([(n, 0)])
visited[0].add(n)

answer = -1
while queue:
    n, cnt = queue.popleft()
    if cnt == K:
        answer = max(answer, int(n))
        continue
    
    for i in range(M-1):
        for j in range(i+1, M):
            arr = list(n)
            if i == 0 and arr[j] == '0':
                continue
            arr[i], arr[j] = arr[j], arr[i]
            new_n = ''.join(arr)
            if new_n not in visited[cnt+1]:
                visited[cnt+1].add(new_n)
                queue.append((new_n, cnt+1))

print(answer)