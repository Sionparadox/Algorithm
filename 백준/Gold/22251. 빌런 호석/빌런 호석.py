import sys
input = sys.stdin.readline

LED = [[0]*10 for _ in range(10)]
segment = ['1110111','0010010','1011101','1011011','0111010','1101011','1101111','1010010','1111111','1111011']
for i in range(9):
    for j in range(i+1, 10):
        for k in range(7):
            LED[i][j] += abs(int(segment[i][k])-int(segment[j][k]))
            LED[j][i] += abs(int(segment[i][k])-int(segment[j][k]))

N, K, P, X = map(int, input().split())

origin = str(X).rjust(K, '0')
answer = 0

for i in range(1, N+1):
    s = str(i).rjust(K, '0')
    cnt = 0
    for k in range(0, K):
        cnt += LED[int(origin[k])][int(s[k])]
    if cnt <= P:
        answer += 1

print(answer-1)
        
        
    