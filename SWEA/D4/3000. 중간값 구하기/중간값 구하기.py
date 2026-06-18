import heapq
MOD = 20171109

def add(n):
    if not high or n <= -low[0]:
        heapq.heappush(low, -n)
    else:
        heapq.heappush(high, n)

    if len(low) > len(high)+1:
        heapq.heappush(high, -heapq.heappop(low))
    elif len(high) > len(low):
        heapq.heappush(low, -heapq.heappop(high))
        
    
TC = int(input())
for tc in range(1, TC+1):
    N, A = map(int, input().split())
    high, low = [], [-A] 
    answer = 0
    
    for _ in range(N):
        x, y = map(int, input().split())
        add(x)
        add(y)
        answer = (answer - low[0])%MOD
    
    print(f'#{tc} {answer}')

#high : 중간보다 큰 수 (최소힙), low : 중간보다 작은 수 (최대힙)