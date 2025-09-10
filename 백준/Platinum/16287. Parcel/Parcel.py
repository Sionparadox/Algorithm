import sys
input = sys.stdin.readline

W, N = map(int, input().split())
nums = list(map(int, input().split()))

S = [None]*(W+1)
for i in range(N-1):
    for j in range(i+1, N):
        w = nums[i]+nums[j]
        if w<=W:
            S[w] = (i, j)

def check():
    for i in range(N-1):
        for j in range(i+1, N):
            w = nums[i]+nums[j]
            if w<=W and S[W-w] is not None:
                if i not in S[W-w] and j not in S[W-w]:
                    return "YES"

    return "NO"

print(check())