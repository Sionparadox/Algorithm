def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    
    gcd, x, y = extended_gcd(b, a%b)
    x, y = y, x-(a//b)*y
    
    return gcd, x, y
    

TC = int(input())
for tc in range(1, TC+1):
    A, B = map(int, input().split())
    gcd, x, y = extended_gcd(A, B)
    print(f'#{tc} {x} {y}')