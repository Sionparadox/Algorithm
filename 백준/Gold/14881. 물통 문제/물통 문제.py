import sys
input = sys.stdin.readline

def GCD(x, y):
    while y:
        x, y = y, x%y
    
    return x
    
T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    
    if c <= max(a,b) and c % GCD(a, b) == 0:
        print("YES")
    else:
        print("NO")
        
'''
5, 3 -> (5, 3, 2, 1, 4, 8, 7, 6)
6, 3 -> (3, 6, 9)
6, 8 -> (6, 8, 2, 4, 10, 12, 14)
gcd의 배수?
'''