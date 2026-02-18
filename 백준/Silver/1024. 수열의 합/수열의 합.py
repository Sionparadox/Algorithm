import sys
import math
input = sys.stdin.readline

N, L = map(int, input().split())

while (N-L*(L-1)/2 >= 0 and L<=100):
    if L%2==1 and N%L==0:
        print(*range(N//L-L//2, N//L+L//2+1))
        break
    elif L%2==0 and N%L == L//2:
        print(*range(N//L-L//2+1, N//L+L//2+1))
        break
    L += 1
else:
    print(-1)

'''
정수가 되려면? 
L이 홀수일 때 N/L도 정수여야함. N%L==0
L이 짝수일 때 N/L=x.5여야함. N%L == L//2

x 부터 길이 L의 수열 합 = Lx + (0~L-1합) = Lx+L*(L-1)/2 = N
N-L*(L-1)/2 >= 0
'''