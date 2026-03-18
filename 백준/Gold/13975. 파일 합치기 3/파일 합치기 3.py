import sys, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    pq = []
    for n in arr:
        heapq.heappush(pq, n)
    
    answer = 0
    for _ in range(K-1):
        x = heapq.heappop(pq)
        y = heapq.heappop(pq)
        answer += x+y
        heapq.heappush(pq, x+y)
    print(answer)