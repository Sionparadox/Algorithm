import sys
input = sys.stdin.readline

def getMax(N):
    L = N//2-1
    res = ''
    if N%2 == 1:
        res += '7'
    else:
        res += '1'
    res += '1'*L
    return res


T = int(input())
testcase = [int(input()) for _ in range(T)]
L = max(testcase)
dp = [-1]*(L+1)
dp[2:12] = [1,7,4,2,6,8,10,18,22,20]

for i in range(12, L+1):
    dp[i] = dp[i-7]*10+8

for num in testcase:
    maxVal = getMax(num) 
    minVal = str(dp[num])
    if minVal[1:3] == '28':
        minVal = minVal[0]+'00'+minVal[3:]
    print(minVal, maxVal)
    
'''
2  : 1
3  : 7
4  : 4
5  : 2
6  : 6(0)
7  : 8
8  : 10
9  : 18
10 : 22
11 : 20
12 : 28
13 : 68
14 : 88
15 : 108
16 : 188
17 : 228
18 : 208
19 : 288
20 : 688
21 : 888
22 : 1088
'''
