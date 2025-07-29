import sys
import heapq
input = sys.stdin.readline

N = int(input())
left = []
right = []
for _ in range(N):
    k = int(input())
    
    if not left or k <= -left[0]:
        heapq.heappush(left, -k)
    else:
        heapq.heappush(right, k)
    
    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))
    
    print(-left[0])

'''
left는 최대힙
right는 최소힙
중간값을 -left[0]으로 참조
'''