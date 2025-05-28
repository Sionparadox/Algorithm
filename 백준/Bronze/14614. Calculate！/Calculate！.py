import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

if C % 2 != 0:
    A = A^B
print(A)