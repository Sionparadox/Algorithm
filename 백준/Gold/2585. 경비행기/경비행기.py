import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
stations = [tuple(map(int, input().split())) for _ in range(N)]


def BFS(d):
    queue = deque([(0, 0)])
    res = 0
    visited = [False]*N
    while queue:
        res += 1
        if res>K+1:
            return False
        for _ in range(len(queue)):
            x, y = queue.popleft()    
            if (10000-x)**2 + (10000-y)**2 <=(10*d)**2:
                return True
            for s in range(N):
                if visited[s]: continue
                nx, ny = stations[s]
                if (nx-x)**2 + (ny-y)**2 <=(10*d)**2:
                    visited[s] = True
                    queue.append((nx, ny))
    return False

left = 2
right = 1415
answer = 0

while left <= right:
    mid = (left+right)//2
    under_k = BFS(mid)
    
    if under_k:
        answer = mid
        right = mid-1
    else:
        left = mid+1

print(answer)


'''
(k+1)개 이하의 간선을 사용해서 노드간 거리의 최대값이 최소로 하는 경우 찾기
이분탐색?
최소 >=2, 최대 <= 1415
mid 이하로 목적지로 갈 때 필요한 횟수 구하기 << BFS?

'''