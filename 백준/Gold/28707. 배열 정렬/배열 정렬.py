import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
end = tuple(sorted(nums))
nums = tuple(nums)
M = int(input())
ops = [list(map(int, input().split())) for _ in range(M)]

dist = defaultdict(lambda:float('inf'))
pq = []
dist[nums] = 0
heapq.heappush(pq, (0, nums))

def swap(nums, u, v):
    nums = list(nums)
    nums[u-1], nums[v-1] = nums[v-1], nums[u-1]
    return tuple(nums)

answer = -1
while pq:
    cost, curr = heapq.heappop(pq)
    
    if curr == end:
        answer = cost
        break
    for u, v, w in ops:
        swapped = swap(curr, u, v)
        if dist[swapped] > cost+w:
            dist[swapped] = cost+w
            heapq.heappush(pq, (cost+w, swapped))
        
print(answer)

'''
BFS
dist = {}
dist[튜플] : 비용
이후 스왑 연산에 대해 연산 비용이 저장된 비용보다 작다면 dist갱신하고 우선순위 큐에 넣기

'''