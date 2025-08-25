import sys
input = sys.stdin.readline
MAX = 360_000

def make_pi(arr):
    L = len(arr)
    pi = [0]*L
    
    j = 0
    for i in range(1, L):
        while j>0 and arr[i] != arr[j]:
            j = pi[j-1]
        if arr[i] == arr[j]:
            j += 1
            pi[i] = j
    return pi

def solve(angles, pattern):
    L = len(angles)
    P = len(pattern)
    pi = make_pi(pattern)
    
    pidx = 0
    for idx in range(L):
        while pidx > 0 and angles[idx] != pattern[pidx]:
            pidx = pi[pidx-1]
        
        if angles[idx] == pattern[pidx]:
            if pidx == P-1:
                return True
            else:
                pidx += 1
    
    return False

N = int(input())
c1 = sorted(list(map(int, input().split())))
c2 = sorted(list(map(int, input().split())))

diff = [c1[i]-c1[i-1] for i in range(1, N)]
angles = diff+[(c1[0] - c1[-1])%MAX]+diff
pattern = [c2[i]-c2[i-1] for i in range(1, N)]

print('possible' if solve(angles, pattern) else 'impossible')