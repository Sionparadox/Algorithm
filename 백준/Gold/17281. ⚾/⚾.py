import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
hit_info = [list(map(int, input().split())) for _ in range(N)]

def simulate(order):
    res = 0
    now = 0
    
    for info in hit_info:
        outs = 0
        base1 = base2 = base3 = 0
        
        while outs < 3:
            hit = info[order[now]]
            
            if hit == 1:
                res += base3
                base3, base2, base1 = base2, base1, 1
            elif hit == 2:
                res += base2 + base3
                base3, base2, base1 = base1, 1, 0
            elif hit == 3:
                res += base1 + base2 + base3
                base3, base2, base1 = 1, 0, 0
            elif hit == 4:
                res += base1 + base2 + base3 + 1
                base1 = base2 = base3 = 0
            else:
                outs += 1
            now = (now+1)%9
    
    return res

answer = 0
for p in permutations(range(1, 9)):
    order = p[:3] + (0,) + p[3:]
    answer = max(answer, simulate(order))

print(answer)