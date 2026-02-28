import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def GCD(x, y):
    if y == 0:
        return x
    return GCD(y, x%y)

gcd = GCD(A, B)
print(gcd)
print(A*B//gcd)