import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

pq = []
for n in nums:
    heapq.heappush(pq, n)

for _ in range(M):
    x = heapq.heappop(pq)
    y = heapq.heappop(pq)
    heapq.heappush(pq, x+y)
    heapq.heappush(pq, x+y)
    
answer = 0
while pq:
    answer += heapq.heappop(pq)

print(answer)
