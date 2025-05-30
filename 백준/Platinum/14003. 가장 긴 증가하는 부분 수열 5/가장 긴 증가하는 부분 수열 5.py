import sys
import bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = []
pos = [0]*N
for i in range(N):
    idx = bisect.bisect_left(dp, A[i])
    
    if idx == len(dp):
        dp.append(A[i])
    else :
        dp[idx] = A[i]
    pos[i] = idx

k = len(dp)-1
answer = []
for i in range(N-1, -1, -1):
    if pos[i] == k:
        answer.append(A[i])
        k -= 1
        if k < 0:
            break

print(len(dp))
print(' '.join(map(str, answer[::-1])))

'''
dp[i] : 길이 i+1인 LIS의 끝 원소중 가장 작은 값
'''
