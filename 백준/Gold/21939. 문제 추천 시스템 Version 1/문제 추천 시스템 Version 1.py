import sys
import heapq
input = sys.stdin.readline

N = int(input())
low = []
high = []
problems = {}
solved = set()

def ADD(p, l):
    heapq.heappush(low, (l, p))
    heapq.heappush(high, (-l, -p))
    problems[p] = l
    
def SOLVED(p):
    l = problems[p]
    solved.add((p, l))

def RECOMMEND(x):
    if x == -1:
        l, p = low[0]
        while (p, l) in solved:
            l, p = heapq.heappop(low)
        heapq.heappush(low, (l, p))
    else:
        l, p = high[0]
        l, p = -l, -p
        while (p, l) in solved:
            l, p = heapq.heappop(high)
            l, p = -l, -p
        heapq.heappush(high, (-l, -p))
    print(p)

for _ in range(N):
    P, L = map(int, input().split())
    ADD(P, L)

M = int(input())
for _ in range(M):
    cmd = list(input().strip().split())
    if cmd[0] == 'add':
        ADD(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'solved':
        SOLVED(int(cmd[1]))
    else:
        RECOMMEND(int(cmd[1]))

        
