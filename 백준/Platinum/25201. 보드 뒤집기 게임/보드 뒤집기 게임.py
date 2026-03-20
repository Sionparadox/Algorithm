import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rows = [0]* 100001
cols = [0]* 100001

for _ in range(N):
    r, c = map(int, input().split())
    rows[r] += 1
    cols[c] += 1

for _ in range(M):
    r, c = map(int, input().split())
    rows[r] += 1
    cols[c] += 1

for i in range(100001):
    if rows[i] % 2 == 1 or cols[i] % 2 == 1:
        print("NO")
        exit(0)

print("YES")
    
'''
단계 1,2,3,4,5에 대해
1,2,3,4,5는 서로 변환 가능
평행이동과 뒤집기로 변환 가능해야함
평행이동 : 짝수개의 붉은칸은 평행이동 가능
뒤집기: 2가지 경우
    10 <->  01 
    01      10
    
    11 <->  00
    01      10
    
각 행, 열의 붉은색이 짝수인지는 변화없음.
'''