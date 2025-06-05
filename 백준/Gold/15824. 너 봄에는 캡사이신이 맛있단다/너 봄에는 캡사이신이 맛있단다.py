import sys
input = sys.stdin.readline
MOD = 1000000007

N = int(input())
menu = list(map(int, input().split()))
menu.sort()
diff = [0]
for i in range(N//2):
    diff.append(diff[-1]+menu[N-i-1]-menu[i])

diff = diff[1:]
if N%2 == 0:
    diff += diff[:-1][::-1]
else :
    diff += diff[::-1]

pow2 = [1]
for i in range(1,N-1):
    pow2.append(pow2[-1]*2%MOD)

answer = 0
for i in range(N-1):
    answer += diff[i]*pow2[i]%MOD
print(answer%MOD)

'''
N//2 길이의 diff 배열을 생성. (누적합 방식)

diff에 diff를 뒤집은 배열을 덧붙임.
이후 아래 식 적용해서 합을 구함
(1<<i)*diff[i]


1 4 5 6 7 10

양쪽 끝의 차 * (1<<사이 개수)
사이 개수 : 4 -> 16*(10-1)                  = 16*9
사이 개수 : 3 -> 8*(10-4+7-1)               = 8*12
사이 개수 : 2 -> 4*(10-5+7-4+6-1)           = 4*13
사이 개수 : 1 -> 2*(10-6+7-5+6-4+5-1)       = 2*12
사이 개수 : 0 -> 1*(10-7+7-6+6-5+5-4+4-1)   = 1*9

leftSum, rightSum을 구함
leftSum = [1, 5, 10]
rightSum = [10, 17, 23]
diff = [9, 12, 13]
diff += diff[:-1][::-1]
(1<<i)*diff[i]

2 5 7 8 9
사이 개수 : 3 -> 8*(9-2)                = 8*7
사이 개수 : 2 -> 4*(9-5+8-2)            = 4*10
사이 개수 : 1 -> 2*(9-7+8-5+7-2)        = 2*10
사이 개수 : 0 -> 1*(9-8+8-7+7-5+5-2)    = 1*7

leftSum, rightSum을 구함
leftSum = [2, 7]
rightSum = [9, 17]
diff = [7, 10] (for문 한번으로 만들 수 있음. << O(N/2))
diff += diff[::-1]
diff = [7,10,10,7]
(1<<i)*diff[i]
'''