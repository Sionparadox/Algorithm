import sys
from collections import deque
input = sys.stdin.readline

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

weight = 0
queue = deque()
idx = 0
time = 0
while idx<N:
    time += 1
    if queue and time-queue[0][1] >= W:
        truck, t = queue.popleft()
        weight -= truck
    
    if trucks[idx]+weight <= L:
        queue.append((trucks[idx], time))
        weight += trucks[idx]
        idx += 1
    
if queue:
    time += W
print(time)
