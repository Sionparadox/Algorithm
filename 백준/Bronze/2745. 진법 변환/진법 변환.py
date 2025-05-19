import sys
input = sys.stdin.readline

N, B = input().split()
B = int(B)
answer = 0
for i in range(1,len(N)+1):
    c = N[-i]
    try:
        c = int(c)
    except ValueError:
        c = ord(c)-ord('A')+10
    answer += c * (B**(i-1))
print(answer)