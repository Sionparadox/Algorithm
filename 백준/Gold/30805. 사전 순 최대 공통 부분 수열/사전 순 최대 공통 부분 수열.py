import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

dp = [[[]for _ in range(M+1)] for _ in range(N+1)]

def compare(x, y):
    xl = len(x)
    yl = len(y)
    for i in range(min(xl, yl)):
        if x[i] > y[i]:
            return True
        elif x[i] < y[i]:
            return False
    return xl>=yl

def makeSequence(origin, new):
    for i in range(len(origin)-1, -1, -1):
        if origin[i] >= new[0]:
            return origin[:i+1]+new
    return new

for i in range(1, N+1):
    for j in range(1, M+1):
        if A[i-1] == B[j-1]:
            arr = dp[i-1][j-1]+[A[i-1]]
            arr2 = makeSequence(dp[i-1][j-1], [A[i-1]])
            if compare(arr, arr2):
                dp[i][j] = arr
            else :
                dp[i][j] = arr2
        else:
            if compare(dp[i-1][j], dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[N][M]))
print(' '.join(map(str, dp[N][M])))