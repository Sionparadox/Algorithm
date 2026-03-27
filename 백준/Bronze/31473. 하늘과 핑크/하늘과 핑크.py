import sys
input = sys.stdin.readline

N = int(input())
A = sum(map(int, input().split()))
B = sum(map(int, input().split()))
print(B, A)