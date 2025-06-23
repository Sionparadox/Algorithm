import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def calc(exp):
    exp = exp.replace(' ','')
    res = 0
    pm = 1
    temp = 0
    for c in exp:
        if c.isalnum():
            temp = temp*10 + int(c)
        else:
            res += pm*temp
            temp = 0
            if c == '+':
                pm = 1
            else:
                pm = -1
    res += pm*temp
    return res

def backTrack(k, exp):
    if k == N+1:
        if calc(exp) == 0:
            result.append(exp)
        return
    
    backTrack(k+1, f'{exp}+{k}')
    backTrack(k+1, f'{exp}-{k}')
    backTrack(k+1, f'{exp} {k}')

T = int(input())
for _ in range(T):
    N = int(input())
    result = []
    backTrack(2, '1')
    result.sort()
    print('\n'.join(result))
    print()
