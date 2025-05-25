import sys
input = sys.stdin.readline
str = input().strip()
L = len(str)

def isPalindrome(s,e):
    while s<=e:
        if str[s] != str[e]:
            return False
        s += 1
        e -= 1
    return True

length = [[] for _ in range(L)]
for i in range(L):
    for j in range(0, i+1):
        if isPalindrome(j, i):
            length[i].append(i-j+1)

dp = [float('inf')]*(L+1)
dp[0] = 0
for i in range(1,L+1):
    for l in length[i-1]:
        dp[i] = min(dp[i], dp[i-l]+1)
print(dp[L])

'''
ABCBADABC
length 배열을 만듬
length[i] : i-length[i] ~ i 범위에 대해 펠린드롬을 만족하는 모든 값.
dp[i] : dp[i-length[i]]+1
         [A,B,C,B,A,D,A,B,C]
length = [1,1,1,3,5,1,3,5,7]
dp =     [1,2,3,2,1,2,3,4,3]
'''
